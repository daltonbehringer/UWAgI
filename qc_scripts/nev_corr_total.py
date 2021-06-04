import uwagi
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
from uwagi import data_corr

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'dejavusans'
matplotlib.rc('font', family='sans serif')

font = {'family': 'sans serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
labelsize = 12

'''
USAGE: iop -> 1-24
	   leg -> beginning at 1, # of legs vary per IOP, will return error if leg doesn't exist
	   test -> refer to uwagi.data_corr.nev_corr() usage comments

	   min_part_size -> minimum ice particle size to include in μm
'''

iop  = 24
leg  = 12
test = 1

min_part_size = 100.

indir = '/Users/jbehrin1/Desktop/snowie_data/allKA/'
outdir = '/Users/jbehrin1/Desktop/snowie_data/'
filename_ka = uwagi.get_times(iop) + '.c1.nc'
filename_sd = uwagi.get_times(iop) + '.SD.cdf'
ka = uwagi.read_ka(indir + filename_ka)
sd = uwagi.read_sd(indir + filename_sd)

### use specific start/end if looking at specific segment, use uwagi.get_times() to view entire leg
# start, end = '203209', '204610'
start, end = uwagi.get_times(iop, leg=leg)[0], uwagi.get_times(iop, leg=leg)[1]

### index start/end in file
p_start = np.where(np.array(ka.fields['HHMMSS']) == start)[0][0]
p_end = np.where(np.array(ka.fields['HHMMSS']) == end)[0][0]

### get cdp and orig nevzorov data
nev = ka.fields['nev_twc'][p_start:p_end]
cdp = ka.fields['cdp_lwc'][p_start:p_end]

### get time of interest from lwc probes and size dist files, initiate 2DS size dist
time = ka.fields['time'][p_start:p_end]
t = sd.time[p_start:p_end]
sd_2ds = np.zeros((30,p_end-p_start))

### get 2DS size dist from rebinned data
for i in range(p_end-p_start):
	sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[i], t[i], 1)[1], data_corr.sd_corr(sd, t[i], t[i], 1)[4]

### threshold 2DS using min_part_size and initialize concentration array
part_ind = np.where(sd_bins[0] > min_part_size)
bin_dD_2ds = (sd_bins[2] - sd_bins[0])[part_ind]
sd_2ds_thres = np.squeeze(sd_2ds[part_ind,:])
conc_2ds = np.zeros((p_end-p_start))

### calculate 2DS concentration based on min_part_size threshold and new 2DS bins
for i in range(p_end-p_start):
	conc_2ds[i] = np.nansum(sd_2ds_thres[:,i] * bin_dD_2ds)

### get 2DP concentration (not rebinned)
conc_2dp = sd.fields['conc_2DP'][p_start:p_end]

### set nan concentrations to 0 and create ice array (ice = 1, no ice = 0) from 2DP and thresholded 2DS
conc_2ds[np.isnan(conc_2ds)] = 0
conc_2dp[np.isnan(conc_2dp)] = 0
ind = np.where(np.logical_or(conc_2ds > 0.001, conc_2dp > 0.001))[0]
ice = np.zeros_like(nev)
ice[ind] = 1

'''
CORRECTION CODE
IF NO ICE, OR CDP DOES NOT = 0 AT ANY POINT, WILL RETURN ERROR.
COMMENT OUT AND CONTINUE TO PLOT, BUT BE CAUTIOUS WITH CORRECTIONS IN THIS CASE!!
'''
ind0 = np.where(np.logical_and(cdp == 0, ice == 0))[0]
mean_diff = np.round(np.mean(cdp[ind0] - nev[ind0]), decimals=4)
print('START_CORR: ' + str(t[ind0[0]]))
print('END_CORR: ' + str(t[ind0[-1]]))
print('DIFF: ' + str(mean_diff))

# ind0 = np.where(cdp == 0)[0]
# mean_diff = np.round(np.mean(cdp[ind0] - nev[ind0]), decimals=4)
# print('START_CORR: ' + str(t[ind0[0]]))
# print('END_CORR: ' + str(t[ind0[-1]]))
# print('DIFF: ' + str(mean_diff))

### get corrected nevzorov data
nev_new = data_corr.nev_corr(ka, iop, var='twc', test_flag=test)[p_start:p_end]

nev_new[nev_new == -9999] = np.nan

### PLOT ###
fig = plt.figure(figsize=(10,4))
ax1 = plt.gca()

x_fmt = DateFormatter("%H%M%S")
ax1.xaxis.set_major_formatter(x_fmt)
ax1.xaxis.set_major_locator(MinuteLocator(interval=2))
ax1.xaxis.set_minor_locator(MinuteLocator(interval=1))

ax1.plot(time, nev, 'r--', linewidth = .75, label = 'Nevzorov')
ax1.plot(time, cdp, 'k:', linewidth = .75, label = 'CDP')
ax1.plot(time, nev_new, 'r-', linewidth = 1, label = 'Corr. Nevzorov')
ax1.plot(time[ind], nev_new[ind], 'bx', markersize = 5, label = r'Ice > 100 $\mu m$')

ax1.set_xlim([time[0], time[-1]])
ax1.set_ylim([np.nanmin(nev)-0.1, np.nanmax(nev_new)+0.1])

ax1.legend()
ax1.set_title('Total Water Content Correction' + '\n'
	+ 'IOP ' + str(iop) + ' | ' + str(start) + ' - ' + str(end), fontdict = font)
ax1.set_ylabel(r'Water Content (g$\/$m$^{-3}$)', fontdict = font)
ax1.set_xlabel('Time (HHMMSS, UTC)', fontdict = font)

ax1.grid(True)
ax1.tick_params(axis='both', which='major', direction='in', grid_linestyle='-', grid_alpha=0.5,
    length=7, labelsize=labelsize)
ax1.tick_params(axis='both', which='minor', direction='in', length=4)

# ax2 = ax1.twinx()

# ax2.plot(time, diff, 'b--', linewidth = 1, label = 'Diff')
# ax2.set_ylim([-0.02,0.02])

# ax2.grid(True)
# ax2.tick_params(axis='both', which='major', direction='in', grid_linestyle='--', grid_alpha=0.75,
#     length=7, labelsize=12)
# ax2.tick_params(axis='both', which='minor', direction='in',length=4)


# plt.savefig(outdir + 'nev_corr_twc_' + str(iop) + 
# 	'_' + str(start) + '_' + str(end), dpi=300, 
# 	bbox_inches = 'tight', pad_inches = 0.1)

plt.show()
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

iop  = 24
leg  = 13
test = 1

indir = '/Users/jbehrin1/Desktop/snowie_data/allKA/'
outdir = '/Users/jbehrin1/Desktop/snowie_data/'
filename = uwagi.get_times(iop) + '.c1.nc'
ka = uwagi.read_ka(indir + filename)

# start, end = '162630', '164800'
start, end = uwagi.get_times(iop, leg=leg)[0], uwagi.get_times(iop, leg=leg)[1]

p_start = np.where(np.array(ka.fields['HHMMSS']) == start)[0][0]
p_end = np.where(np.array(ka.fields['HHMMSS']) == end)[0][0]

nev = ka.fields['nev_lwc'][p_start:p_end]
cdp = ka.fields['cdp_lwc'][p_start:p_end]

time = ka.fields['time'][p_start:p_end]

'''
CORRECTION CODE
'''
ind0 = np.where(cdp == 0)[0]
mean_diff = np.round(np.mean(cdp[ind0] - nev[ind0]), decimals=4)
print('START_CORR: ' + str(time[ind0[0]]))
print('END_CORR: ' + str(time[ind0[-1]]))
print('DIFF: ' + str(mean_diff))

# ind0 = np.where(ice == 0)
# mean_diff = np.round(np.mean(cdp[ind0] - nev[ind0]), decimals=4)
# print('DIFF: ' + str(mean_diff))

nev_new = data_corr.nev_corr(ka, iop, var='lwc', test_flag=test)[p_start:p_end]

nev_new[nev_new == -9999] = np.nan

fig = plt.figure(figsize=(10,4))
ax1 = plt.gca()

x_fmt = DateFormatter("%H%M%S")
ax1.xaxis.set_major_formatter(x_fmt)
ax1.xaxis.set_major_locator(MinuteLocator(interval=2))
ax1.xaxis.set_minor_locator(MinuteLocator(interval=1))

ax1.plot(time, nev, 'r--', linewidth = .75, label = 'Nevzorov')
ax1.plot(time, cdp, 'k:', linewidth = .75, label = 'CDP')
ax1.plot(time, nev_new, 'r-', linewidth = 1, label = 'Corr. Nevzorov')

ax1.set_xlim([time[0], time[-1]])
ax1.set_ylim([np.nanmin(nev)-0.05, np.nanmax(cdp)+0.05])

ax1.legend()
ax1.set_title('Liquid Water Content Correction' + '\n'
	+ 'IOP ' + str(iop) + ' | ' + str(start) + ' - ' + str(end), fontdict = font)

ax1.set_ylabel(r'Water Content (g$\/$m$^{-3}$)', fontdict = font)
ax1.set_xlabel('Time (HHMMSS, UTC)', fontdict = font)

ax1.grid(True)
ax1.tick_params(axis='both', which='major', direction='in', grid_linestyle='-', grid_alpha=0.5,
    length=7, labelsize=labelsize)
ax1.tick_params(axis='both', which='minor', direction='in',length=4)

# ax2 = ax1.twinx()

# ax2.plot(time, diff, 'b--', linewidth = 1, label = 'Diff')
# ax2.set_ylim([-0.02,0.02])

# ax2.grid(True)
# ax2.tick_params(axis='both', which='major', direction='in', grid_linestyle='--', grid_alpha=0.75,
#     length=7, labelsize=12)
# ax2.tick_params(axis='both', which='minor', direction='in',length=4)


# plt.savefig(outdir + 'nev_corr_lwc_' + str(iop) + 
# 	'_' + str(start) + '_' + str(end), dpi=300, 
# 	bbox_inches = 'tight', pad_inches = 0.1)

plt.show()
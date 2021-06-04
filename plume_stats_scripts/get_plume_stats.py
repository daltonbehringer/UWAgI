import uwagi
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
from uwagi import data_corr
import matplotlib.ticker as ticker


font = {'family': 'sans serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
labelsize = 12

iop        = 5
leg        = 10
out_dist   = 4.5 ### km
plume_flag = 0 ### 0 = entire leg, 1 = in-plume only, 2 = out-of-plume only
var        = 'lwc'

min_part_size = 100. ### μm

indir = '/Users/jbehrin1/Desktop/snowie_data/allKA/'
outdir = '/Users/jbehrin1/Desktop/snowie_data/'
filename_ka = uwagi.get_times(iop) + '.c1.nc'
filename_sd = uwagi.get_times(iop) + '.SD.cdf'
ka = uwagi.read_ka(indir + filename_ka)
sd = uwagi.read_sd(indir + filename_sd)

start, end = uwagi.get_times(iop, leg=leg)[0], uwagi.get_times(iop, leg=leg)[1]

t = np.array(ka.fields['HHMMSS']).astype(int)

p_start = np.where(t == int(start))[0][0]
p_end = np.where(t == int(end))[0][0]

if plume_flag is 0:

	print ('Entire Leg ' + str(leg))
	time = ka.fields['time'][p_start:p_end]
	nev = ka.fields['nev_lwc'][p_start:p_end]
	nev_new = data_corr.nev_corr(ka, iop, var=var)[p_start:p_end]
	nev_new_ice = data_corr.nev_corr(ka, iop, var='iwc')[p_start:p_end]
	nev_new_twc = data_corr.nev_corr(ka, iop, var='twc')[p_start:p_end]
	cdp = ka.fields['cdp_lwc'][p_start:p_end]
	cdp_conc = ka.fields['cdp_conc'][p_start:p_end]

	sd_2ds = np.zeros((30,p_end-p_start))
	t = sd.time[p_start:p_end]

	for i in range(p_end-p_start):
		sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[i], t[i], 1)[1], data_corr.sd_corr(sd, t[i], t[i], 1)[4]

	part_ind = np.where(sd_bins[0] > min_part_size)
	bin_dD_2ds = (sd_bins[2] - sd_bins[0])[part_ind]
	sd_2ds_thres = np.squeeze(sd_2ds[part_ind,:])
	conc_2ds = np.zeros((p_end-p_start))

	for i in range(p_end-p_start):
		conc_2ds[i] = np.nansum(sd_2ds_thres[:,i] * bin_dD_2ds)

	conc_2dp = sd.fields['conc_2DP'][p_start:p_end]

elif plume_flag is 1:

	print ('Inside Plume')
	p_ind = uwagi.get_plume(ka, iop, leg)[0]
	time = ka.fields['time'][p_ind]
	nev = ka.fields['nev_lwc'][p_ind]
	nev_new = data_corr.nev_corr(ka, iop, var=var)[p_ind]
	cdp = ka.fields['cdp_lwc'][p_ind]
	cdp_conc = ka.fields['cdp_conc'][p_ind]

	sd_2ds = np.zeros((30,len(p_ind)))
	t = sd.time

	for i in range(len(p_ind)):
		sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[p_ind[i]], t[p_ind[i]], 1)[1], data_corr.sd_corr(sd, t[p_ind[i]], t[p_ind[i]], 1)[4]

	part_ind = np.where(sd_bins[0] > min_part_size)
	bin_dD_2ds = (sd_bins[2] - sd_bins[0])[part_ind]
	sd_2ds_thres = np.squeeze(sd_2ds[part_ind,:])
	conc_2ds = np.zeros((len(p_ind)))

	for i in range(len(p_ind)):
		conc_2ds[i] = np.nansum(sd_2ds_thres[:,i] * bin_dD_2ds)

	conc_2dp = sd.fields['conc_2DP'][p_ind]

elif plume_flag is 2:

	print ('Outside Plume')
	p_ind = uwagi.get_out_plume(ka, iop, leg, out_dist)[0]
	# print (p_ind)
	time = ka.fields['time'][p_start:p_end][p_ind]
	nev = ka.fields['nev_lwc'][p_ind]
	nev_new = data_corr.nev_corr(ka, iop, var=var)[p_ind]
	cdp = ka.fields['cdp_lwc'][p_ind]
	cdp_conc = ka.fields['cdp_conc'][p_ind]

	sd_2ds = np.zeros((30,len(p_ind)))
	t = sd.time[p_start:p_end][p_ind]

	for i in range(len(p_ind)):
		sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[i], t[i], 1)[1], data_corr.sd_corr(sd, t[i], t[i], 1)[4]

	part_ind = np.where(sd_bins[0] > min_part_size)
	bin_dD_2ds = (sd_bins[2] - sd_bins[0])[part_ind]
	sd_2ds_thres = np.squeeze(sd_2ds[part_ind,:])
	conc_2ds = np.zeros((len(p_ind)))

	for i in range(len(p_ind)):
		conc_2ds[i] = np.nansum(sd_2ds_thres[:,i] * bin_dD_2ds)

	conc_2dp = sd.fields['conc_2DP'][p_ind]

in_ind = uwagi.get_plume(ka, iop, leg)
out_ind = uwagi.get_out_plume(ka, iop, leg, out_dist)

	# nev[p_ind] = np.nan
	# nev_new[p_ind] = np.nan
	# cdp[p_ind] = np.nan
	# cdp_conc[p_ind] = np.nan
	# conc_2ds[p_ind] = np.nan
	# conc_2dp[p_ind] = np.nan

##ICE THRESHOLDED AT 1/L
conc_2ds[np.isnan(conc_2ds)] = 0
conc_2dp[np.isnan(conc_2dp)] = 0
ind = np.where(np.logical_and(conc_2ds < 0.001, conc_2dp < 0.001))[0]
if len(ind) == len(nev_new_ice):
	raise ValueError('ICE CONCENTRATION TOO LOW')
nev_new_ice[ind] = np.nan
nev_new_twc[ind] = np.nan

##LIQUID THRESHOLD AT 5/cm^3
nev_new[cdp_conc < 5] = np.nan
# nev_new_ice[cdp_conc < 5] = np.nan
nev_new_twc[cdp_conc < 5] = np.nan
cdp[cdp_conc < 5] = np.nan

test_arr_out = np.zeros_like(nev_new)
test_arr_in = np.zeros_like(nev_new)
# test_arr[np.isfinite(nev_new)] = 1
test_arr_in[in_ind] = 1
test_arr_out[out_ind] = 1

fig = plt.figure(figsize=(10,4))
ax1 = plt.gca()

lats = ka.fields['lat'][p_start:p_end]
lons = ka.fields['lon'][p_start:p_end]
d = uwagi.distance.dist(lats, lons)

ax1.plot(d, cdp, 'k-', linewidth = .75, label = 'CDP Liquid')
ax1.plot(d, nev_new, 'r-', linewidth = .75, label = 'Nevzorov Liquid')
ax1.plot(d, nev_new_ice, 'b-', linewidth = .75, label = 'Nevzorov Ice')
ax1.plot(d, nev_new_twc, 'g-', linewidth = .75, label = 'Nevzorov TWC')
ax1.set_xlabel('Distance from PJ (km)', fontdict=font)
ax1.set_xlim([-15,55])
ax1.set_ylim([0,0.4])
ax1.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax1.legend(loc=1)
# ax1.set_title('IOP ' + str(iop) + ' | ' + str(start) + ' - ' + str(end))
ax1.set_title('IOP ' + str(iop) + ' | Leg ' + str(leg) + 
	' | Out-of-Plume Region = ' + str(out_dist) + ' km')

ax1.grid(True)
ax1.tick_params(axis='both', which='major', direction='in', grid_linestyle='-', grid_alpha=0.5,
    length=7, labelsize=12)
ax1.tick_params(axis='both', which='minor', direction='in', length=4)
ax1.set_ylabel(r'Water Content (g$\/$m$^{-3}$)', fontdict=font)

cdp_mean = np.round(np.nanmean(cdp[out_ind]), decimals=3)
cdp_max = np.round(np.nanmax(cdp[out_ind]), decimals=3)
cdp_10 = np.round(np.nanpercentile(cdp[out_ind], 10), decimals=3)
cdp_25 = np.round(np.nanpercentile(cdp[out_ind], 25), decimals=3)
cdp_75 = np.round(np.nanpercentile(cdp[out_ind], 75), decimals=3)
cdp_90 = np.round(np.nanpercentile(cdp[out_ind], 90), decimals=3)

print(' ')
print('CDP')
print(cdp_mean, cdp_max)
print(cdp_10, cdp_25, cdp_75, cdp_90)

nev_mean = np.round(np.nanmean(nev_new[out_ind]), decimals=3)
nev_max = np.round(np.nanmax(nev_new[out_ind]), decimals=3)
nev_10 = np.round(np.nanpercentile(nev_new[out_ind], 10), decimals=3)
nev_25 = np.round(np.nanpercentile(nev_new[out_ind], 25), decimals=3)
nev_75 = np.round(np.nanpercentile(nev_new[out_ind], 75), decimals=3)
nev_90 = np.round(np.nanpercentile(nev_new[out_ind], 90), decimals=3)

print(' ')
print('Nevzorov Liquid')
print(nev_mean, nev_max)
print(nev_10, nev_25, nev_75, nev_90)

nev_mean_i = np.round(np.nanmean(nev_new_ice[out_ind]), decimals=3)
nev_max_i = np.round(np.nanmax(nev_new_ice[out_ind]), decimals=3)
nev_10_i = np.round(np.nanpercentile(nev_new_ice[out_ind], 10), decimals=3)
nev_25_i = np.round(np.nanpercentile(nev_new_ice[out_ind], 25), decimals=3)
nev_75_i = np.round(np.nanpercentile(nev_new_ice[out_ind], 75), decimals=3)
nev_90_i = np.round(np.nanpercentile(nev_new_ice[out_ind], 90), decimals=3)

print(' ')
print('Nevzorov Ice')
print(nev_mean_i, nev_max_i)
print(nev_10_i, nev_25_i, nev_75_i, nev_90_i)

ax2 = ax1.twinx()

ax2.plot(d[test_arr_in == 1], test_arr_in[test_arr_in == 1], 'rx', markersize = 3, label = 'In-Plume')
ax2.plot(d[test_arr_out == 1], test_arr_out[test_arr_out == 1], 'bx', markersize = 3, label = 'Out-of-Plume')
# ax2.set_ylim([-0.02,0.02])
ax2.legend(loc=2)

# ax2.grid(True)
# ax2.xaxis.set_major_formatter(x_fmt)
# ax2.xaxis.set_major_locator(MinuteLocator(interval=2))
ax2.tick_params(axis='both', which='major', direction='in', grid_linestyle='--', grid_alpha=0.75,
    length=0, labelsize=0)
ax2.tick_params(axis='both', which='minor', direction='in',length=4)


# plt.savefig(outdir + 'show_plume_iop' + str(iop) + 
# 	'_leg' + str(leg) + '_' + str(out_dist)[0] + str(out_dist)[2], dpi=300, 
# 	bbox_inches = 'tight', pad_inches = 0.1)
# plt.show()





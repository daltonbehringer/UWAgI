import uwagi
from uwagi import data_corr
from netCDF4 import Dataset
import numpy as np
from datetime import date
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm

print('Generating file for IOP ' + str(sys.argv[1]))
iop = int(sys.argv[1])
# iop = 5 

indir = '/Users/jbehrin1/Desktop/snowie_data/allKA/'
outdir = '/Users/jbehrin1/Desktop/snowie_data/nevcorr/'
filename_ka = uwagi.get_times(iop) + '.c1.nc'
filename_sd = uwagi.get_times(iop) + '.SD.cdf'
ka = uwagi.read_ka(indir + filename_ka)
sd = uwagi.read_sd(indir + filename_sd)

t = np.array(ka.fields['HHMMSS']).astype(int)

nev_liq, liq_flag = uwagi.nev_corr(ka, iop, var='lwc', qc_flag=1)
nev_tot, tot_flag = uwagi.nev_corr(ka, iop, var='twc', qc_flag=1)
nev_ice, ice_flag = uwagi.nev_corr(ka, iop, var='iwc', qc_flag=1)

nev_liq_orig = ka.fields['nev_lwc']
nev_tot_orig = ka.fields['nev_twc']

sd_2ds = np.zeros((30,len(t)))
conc_2ds_100 = np.zeros((len(t)))
conc_2ds_50 = np.zeros((len(t)))

if iop is 3 or iop is 19 or iop is 20:
	print('NO SIZE DIST')
	conc_2ds_100[:] = np.nan
	conc_2ds_50[:] = np.nan

else:
### get 2DS size dist from rebinned data
	print('\n')
	print('Getting size distribution')
	for i in tqdm(range(len(t))):
		sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[i], t[i], 1)[1], data_corr.sd_corr(sd, t[i], t[i], 1)[4]

	# for i in range(len(t)):
	# 	print(i/len(t))
	# 	sd_2ds[:,i], sd_bins = data_corr.sd_corr(sd, t[i], t[i], 1)[1], data_corr.sd_corr(sd, t[i], t[i], 1)[4]

	### threshold 2DS using min_part_size and initialize concentration array
	part_ind = np.where(sd_bins[0] > 100.)
	bin_dD_2ds = (sd_bins[2] - sd_bins[0])
	sd_2ds_thres = np.squeeze(sd_2ds[part_ind,:])

	### calculate 2DS concentration based on min_part_size threshold and new 2DS bins
	print('\n')
	print('Calculating Number Concentration')
	for i in tqdm(range(len(t))):
		conc_2ds_100[i] = np.nansum(sd_2ds_thres[:,i] * bin_dD_2ds[part_ind])
		conc_2ds_50[i] = np.nansum(sd_2ds[:,i] * bin_dD_2ds)

nc = Dataset(outdir + filename_ka[0:-2] + 'nevcorr.nc', 
	mode='w', format='NETCDF3_CLASSIC') 

today = date.today()

nc.Title = 'Manually corrected liquid, total, and ice water content from the Nevzorov probe'
nc.FlightNumber = str(iop)
nc.Contact = 'Dalton Behringer - jbehrin1@uwyo.edu | Jeffrey French - jfrench@uwyo.edu'
nc.CorrectionDate = today.strftime('%B %d, %Y')
nc.OriginalFile = filename_ka
nc.Platform = 'N2UW'

time_dim = nc.createDimension('time', None)
time = nc.createVariable('time', np.intc, ('time',))
time.units = 'UTC'
time.long_name = 'HHMMSS UTC'
time[:] = ka.fields['HHMMSS']

lat = nc.createVariable('lat', np.float32, ('time',))
lat.units = 'degrees_north'
lat.long_name = 'latitude'
lat[:] = ka.fields['lat']

lon = nc.createVariable('lon', np.float32, ('time',))
lon.units = 'degrees_east'
lon.long_name = 'longitude'
lon[:] = ka.fields['lon']

lwcflag = nc.createVariable('lwcflag', np.intc, ('time',))
lwcflag.long_name = 'QC flag for Nevzorov liquid water content, 0=raw, 1=good, 2=suspect'
lwcflag[:] = liq_flag

twcflag = nc.createVariable('twcflag', np.intc, ('time',))
twcflag.long_name = 'QC flag for Nevzorov total water content, 0=raw, 1=good, 2=suspect'
twcflag[:] = tot_flag 

iwcflag = nc.createVariable('iwcflag', np.intc, ('time',))
iwcflag.long_name = 'QC flag for Nevzorov ice water content, 0=raw, 1=good, 2=suspect'
iwcflag[:] = ice_flag

cdplwc = nc.createVariable('cdplwc', np.float32, ('time',))
cdplwc.units = 'gram/m3'
cdplwc.long_name = 'CDP liquid water content'
cdplwc[:] = ka.fields['cdp_lwc']

nevlwc = nc.createVariable('nevlwc', np.float32, ('time',))
nevlwc.units = 'gram/m3'
nevlwc.long_name = 'Nevzorov liquid water content'
nevlwc[:] = nev_liq

nevtwc = nc.createVariable('nevtwc', np.float32, ('time',))
nevtwc.units = 'gram/m3'
nevtwc.long_name = 'Nevzorov total water content'
nevtwc[:] = nev_tot

neviwc = nc.createVariable('neviwc', np.float32, ('time',))
neviwc.units = 'gram/m3'
neviwc.long_name = 'Nevzorov ice water content'
neviwc[:] = nev_ice

conc2ds100 = nc.createVariable('conc2ds100', np.float32, ('time',))
conc2ds100.units = 'cm-3'
conc2ds100.long_name = '2DS Number concentration (100 μm < D < 1000 μm)'
conc2ds100[:] = conc_2ds_100

conc2ds = nc.createVariable('conc2ds50', np.float32, ('time',))
conc2ds.units = 'cm-3'
conc2ds.long_name = '2DS Number concentration (50 μm < D < 1000 μm)'
conc2ds[:] = conc_2ds_50

print('\nFile stored to ' + outdir + filename_ka[0:-2] + 'nevcorr.nc')

nc.close()


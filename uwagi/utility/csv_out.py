import pandas as pd
import numpy as np

from ..utility.data_corr import sd_corr
from ..utility.iop import get_times
from ..readers.read_ka import read_ka
from ..readers.read_sizedist import read_sd
from ..utility.distance import dist

'''

Stores time-averaged size distribution to CSV

'''

def sd_to_csv(
    iop,
    leg = None,
    start = None,
    end = None,
    indir = None,
    outdir = None
    ):

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    # if start is None and end is None and leg is not None:
    #     print('Gathering data from entire leg '+str(leg)+' period.')
    #     start_time, end_time = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    # if start is not None and end is not None and leg is None:
    #     start_time, end_time = get_times(iop, start=start, end=end)[0], get_times(iop, start=start, end=end)[1

    filename = get_times(iop)+'.SD.cdf'

    if indir is not None:
        if indir[-1] is '/':
            sd = read_sd(indir+filename)
        else:
            sd = read_sd(indir+'/'+filename)
    else:
        sd = read_sd(filename)

    if start is None:
        start = int(sd.time[0])
    if end is None:
        end = int(sd.time[-1])

    sd_CDP, sd_2DS, sd_2DP, bins_CDP, bins_2DS, bins_2DP = sd_corr(sd, start, end, 0)

    bin_min = np.append(bins_CDP[0], bins_2DS[0])
    bin_min = np.append(bin_min, bins_2DP[0])

    bin_mid = np.append(bins_CDP[1], bins_2DS[1])
    bin_mid = np.append(bin_mid, bins_2DP[1])

    bin_max = np.append(bins_CDP[2], bins_2DS[2])
    bin_max = np.append(bin_max, bins_2DP[2])

    sd = np.append(sd_CDP, sd_2DS)
    sd = np.append(sd, sd_2DP)

    df = pd.DataFrame(data = None, index = None, columns = None)

    df['bin_min (microns)'] = bin_min
    df['bin_mid (microns)'] = bin_mid
    df['bin_max (microns)'] = bin_max

    df['size_dist (#/cm^3/um)'] = sd

    if outdir is None:
        filename = 'sizedist_'+str(start)+'_'+str(end)+'.csv'
    if outdir is not None:
        if outdir[-1] is '/':
            filename = outdir+'sizedist_'+str(start)+'_'+str(end)+'.csv'
        else:
            filename = outdir+'/sizedist_'+str(start)+'_'+str(end)+'.csv'

    csv_out = df.to_csv(filename, sep = ',', index = False, encoding = 'utf-8')

    print('CSV saved to ' + filename)

    return csv_out

'''

Stores time-series size distribution to CSV

'''

def sd_time_csv(
    iop,
    leg = None,
    start = None,
    end = None,
    indir = None,
    outdir = None
    ):

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Gathering data from entire leg '+str(leg)+' period.')
        start, end = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    # if start is not None and end is not None and leg is None:
    #     start_time, end_time = get_times(iop, start=start, end=end)[0], get_times(iop, start=start, end=end)[1

    filename = get_times(iop)+'.SD.cdf'
    filename_ka = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            sd = read_sd(indir+filename)
            ka = read_ka(indir+filename_ka)
        else:
            sd = read_sd(indir+'/'+filename)
            ka = read_ka(indir+'/'+filename_ka)
    else:
        sd = read_sd(filename)
        ka = read_ka(filename_ka)

    if start is None:
        start = int(sd.time[0])
    if end is None:
        end = int(sd.time[-1])

    p_start = np.where(sd.time == start)[0][0]
    p_end = np.where(sd.time == end)[0][0]

    t = sd.time[p_start:p_end].astype(int)

    sd_CDP = np.zeros((27,len(t)))
    sd_2DS = np.zeros((30,len(t)))
    sd_2DP = np.zeros((18,len(t)))

    for i in range(len(t)):
        sd_CDP[:,i], sd_2DS[:,i], sd_2DP[:,i], bins_CDP, bins_2DS, bins_2DP = sd_corr(sd, t[i], t[i], 1)

    sd = np.append(sd_CDP, sd_2DS, axis=0)
    sd = np.append(sd, sd_2DP, axis=0)

    bin_min = np.append(bins_CDP[0], bins_2DS[0])
    bin_min = np.append(bin_min, bins_2DP[0])

    bin_mid = np.append(bins_CDP[1], bins_2DS[1])
    bin_mid = np.append(bin_mid, bins_2DP[1])

    bin_max = np.append(bins_CDP[2], bins_2DS[2])
    bin_max = np.append(bin_max, bins_2DP[2])

    lats = ka.fields['lat'][p_start:p_end]
    lons = ka.fields['lon'][p_start:p_end]
    d = dist(lats, lons)

    df = pd.DataFrame(data = None, index = None, columns = None)

    df['Time (UTC)'] = t
    df['Seconds since start'] = np.arange(0,len(t))
    df['Dist from PJ (km)'] = d
    df['Latitude'] = lats
    df['Longitude'] = lons

    for j in range(len(bin_mid)):
        sd[j,:][np.isnan(sd[j,:])] = -9999.
        df[str(np.round(bin_mid[j], decimals=0))+' (um)'] = sd[j,:]

    if outdir is None:
        filename = 'sizedist_ts_'+str(start)+'_'+str(end)+'.csv'
    if outdir is not None:
        if outdir[-1] is '/':
            filename = outdir+'sizedist_ts_'+str(start)+'_'+str(end)+'.csv'
        else:
            filename = outdir+'/sizedist_ts_'+str(start)+'_'+str(end)+'.csv'

    csv_out = df.to_csv(filename, sep = ',', index = False, encoding = 'utf-8')

    print('CSV saved to ' + filename)

    return csv_out


'''

Stores time-series of KA variables to CSV

'''

def ts_to_csv(
    iop,
    leg = None,
    start = None,
    end = None,
    indir = None,
    outdir = None
    ):

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Gathering data from entire leg '+str(leg)+' period.')
        start, end = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    filename = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            ka = read_ka(indir+filename)
        else:
            ka = read_ka(indir+'/'+filename)
    else:
        ka = read_ka(filename)

    if start is None:
        start = int(ka.fields['HHMMSS'][0])
    if end is None:
        end = int(ka.fields['HHMMSS'][-1])

    p_start = np.where(np.array(ka.fields['HHMMSS']) == str(start))[0][0]
    p_end = np.where(np.array(ka.fields['HHMMSS']) == str(end))[0][0]

    t = ka.fields['HHMMSS'][p_start:p_end]

    df = pd.DataFrame(data = None, index = None, columns = None)

    df['Time (UTC)'] = t
    df['Seconds since start'] = np.arange(0,len(t))
    df['Latitude'] = ka.fields['lat'][p_start:p_end]
    df['Longitude'] = ka.fields['lon'][p_start:p_end]
    df['Altitude (m)'] = ka.fields['alt'][p_start:p_end]
    df['True Airspeed (m/s)'] = ka.fields['airspeed'][p_start:p_end]
    df['Wind Spd (m/s)'] = ka.fields['wind_mag'][p_start:p_end]
    df['Wind Dir (deg)'] = ka.fields['wind_dir'][p_start:p_end]
    df['Temp (C)'] = ka.fields['temperature'][p_start:p_end]
    df['Dewpoint (C)'] = ka.fields['dewpoint'][p_start:p_end]
    df['CDP LWC (g/m^3)'] = ka.fields['cdp_lwc'][p_start:p_end]
    df['CDP Total Concentration (#/cm^3)'] = ka.fields['cdp_conc'][p_start:p_end]
    df['Nevzerov LWC (g/m^3)'] = ka.fields['nev_lwc'][p_start:p_end]
    df['Nevzerov TWC (g/m^3)'] = ka.fields['nev_twc'][p_start:p_end]

    if outdir is None:
        filename = 'timeseries_IOP'+str(iop)+'_'+str(start)+'_'+str(end)+'.csv'
    if outdir is not None:
        if outdir[-1] is '/':
            filename = outdir+'timeseries_IOP'+str(iop)+'_'+str(start)+'_'+str(end)+'.csv'
        else:
            filename = outdir+'/timeseries_IOP'+str(iop)+'_'+str(start)+'_'+str(end)+'.csv'

    csv_out = df.to_csv(filename, sep = ',', index = False, encoding = 'utf-8')

    print('CSV saved to ' + filename)

    return csv_out

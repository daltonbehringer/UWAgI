import pandas as pd
from ..utility.data_corr import sd_corr

'''

Takes data and stores into a csv file

'''

def sd_to_csv(
    sd,
    start_time = None,
    end_time = None,
    outdir = None
    ):

    if start_time is None:
        start_time = int(sd.time[0])
    if end_time is None:
        end_time = int(sd.time[-1])

    sd_CDP, sd_2DS, sd_2DP, bins_CDP, bins_2DS, bins_2DP = sd_corr(sd, start_time, end_time)

    bin_min = np.append(bins_CDP[0], bins_2DS[0])
    bin_min = np.append(bin_min, bins_2DP[0])
    
    bin_mid = np.append(bins_CDP[1], bins_2DS[1])
    bin_mid = np.append(bin_mid, bins_2DP[1])
    
    bin_max = np.append(bins_CDP[2], bins_2DS[2])
    bin_max = np.append(bin_max, bins_2DP[2])

    sd = np.append(sd_CDP, sd_2DS)
    sd = np.append(sd, sd_2DP)

    # df = pd.DataFrame(data = sd.time.astype(int), index = None, columns = ['HHMMSS'])
    df = pd.DataFrame(data = None, index = None, columns = None)

    df['bin_min'] = bin_min
    df['bin_mid'] = bin_mid
    df['bin_max'] = bin_max
    
    df['size_dist'] = sd

    if outdir is None:
        filename = 'sizedist_'+str(start_time)+'_'+str(end_time)+'.csv'
    if outdir is not None:
        filename = outdir+'sizedist_'+str(start_time)+'_'+str(end_time)+'.csv'

    csv_out = df.to_csv(filename, sep = ',', index = False, enconding = 'utf-8')

    return csv_out

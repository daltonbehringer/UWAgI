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

    df = pd.DataFrame(data = sd.time, index = None, columns = ['HHMMSS'])

    df['bin_min_CDP'], df['bin_mid_CDP'], df['bin_max_CDP'] = bins_CDP[0], bins_CDP[1], bins_CDP[2]
    df['sd_CDP'] = sd_CDP

    df['bin_min_2DS'], df['bin_mid_2DS'], df['bin_max_2DS'] = bins_2DS[0], bins_2DS[1], bins_2DS[2]
    df['sd_2DS'] = sd_2DS

    df['bin_min_2DP'], df['bin_mid_2DP'], df['bin_max_2DP'] = bins_2DP[0], bins_2DP[1], bins_2DP[2]
    df['sd_2DP'] = sd_2DP

    if outdir is None:
        filename = 'sizedist_'+str(start_time)+'_'+str(end_time)+'.csv'
    if outdir is not None:
        filename = outdir+'sizedist_'+str(start_time)+'_'+str(end_time)+'.csv'

    csv_out = df.to_csv(filename, sep = ',', index = False, enconding = 'utf-8')

    return csv_out

'''Includes data corrections and for data from SNOWIE 2017'''

import numpy as np
import pandas as pd

def sd_corr(
    sd,
    start_time,
    end_time,
    t_flag
    ):

    '''
    Adjust size distribution to set new bins
    sd = sd object (output from read_sd)
    t_flag: 0 = time-averaged single size dist, 1 = time-series size dist
    '''


    # bins_2DP = np.arange(100,20300,200)
    # bins1 = np.arange(500,2100,200)
    # bins2 = np.arange(2100,21100,1000)
    # bins_2DP_new = np.append(bins1,bins2)
    # bin_mid_2DP = (bins_2DP[1:] + bins_2DP[0:-1]) / 2
    # bin_min_2DP_new = bins_2DP_new[0:-1]
    # bin_max_2DP_new = bins_2DP_new[1:]
    # bin_dD_2DP = bins_2DP[1:] - bins_2DP[0:-1]

    # bin_mid_2DP_new = (bins_2DP_new[1:] + bins_2DP_new[0:-1]) / 2
    # bin_dD_2DP_new = bins_2DP_new[1:] - bins_2DP_new[0:-1]
    # sd_2DP_new = np.zeros_like(bin_dD_2DP_new)

    bin_mid_CDP = sd.bin_mid_CDP.data
    bin_min_CDP = sd.bin_min_CDP.data
    bin_max_CDP = sd.bin_max_CDP.data

    ind_min = np.arange(5,15)
    ind_min = np.append(ind_min, np.arange(15,35,2))
    ind_min = np.append(ind_min, np.arange(35,59,4))
    ind_min = np.append(ind_min, np.arange(59,83,8))
    ind_min = np.append(ind_min, 83)

    ind_max = np.arange(5,15)
    ind_max = np.append(ind_max, np.arange(16,36,2))
    ind_max = np.append(ind_max, np.arange(38,62,4))
    ind_max = np.append(ind_max, np.arange(66,90,8))
    ind_max = np.append(ind_max, 98)

    bin_min_2DS_new = np.round(sd.bin_min_2DS[ind_min])
    bin_max_2DS_new = np.round(sd.bin_max_2DS[ind_max])
    bin_dD_2DS_new = bin_max_2DS_new - bin_min_2DS_new
    bin_mid_2DS_new = np.round((bin_max_2DS_new + bin_min_2DS_new) / 2).data
    sd_2DS_new = np.zeros_like(bin_mid_2DS_new)
    # ind_re = np.where(bin_mid_2DS_re > 40)
    # ind_driz_re = np.where(np.logical_and(bin_min_2DS_re >= 95, bin_max_2DS_re <= 295))
    # ind_driz = np.where(np.logical_and(bin_mid_2DS >= 95, bin_mid_2DS <= 295))

    if t_flag == 0:
        ind = np.where(np.logical_and(sd.time >= start_time, sd.time < end_time))[0]
        
        sd.dist_CDP[ind,:][sd.dist_CDP[ind,:] == 0.] = np.nan
        sd.dist_2DS[ind,:][sd.dist_2DS[ind,:] == 0.] = np.nan
        sd.dist_2DP[ind,1:][sd.dist_2DP[ind,1:] == 0.] = np.nan

        sd_CDP = np.nanmean(sd.dist_CDP[ind,:], axis=0).data
        sd_2DS = np.nanmean(sd.dist_2DS[ind,:], axis=0).data
        sd_2DP = np.nanmean(sd.dist_2DP[ind,1:], axis=0).data
    
    if t_flag == 1:
        ind = np.where(sd.time == start_time)[0]

        sd_CDP = np.squeeze(sd.dist_CDP[ind,:])
        sd_2DS = np.squeeze(sd.dist_2DS[ind,:])
        sd_2DP = np.squeeze(sd.dist_2DP[ind,1:])

    for i in range(0, len(bin_dD_2DS_new)):
        ind_i = np.where(np.logical_and(sd.bin_mid_2DS >= bin_min_2DS_new[i], sd.bin_mid_2DS <= bin_max_2DS_new[i]))
        sd_2DS_new[i] = np.nansum(sd_2DS[ind_i] * sd.bin_dD_2DS.data[ind_i]) / np.nansum(sd.bin_dD_2DS.data[ind_i])

    # for j in range(0, len(bin_dD_2DP_new)):
    #     ind_j = np.where(np.logical_and(sd.bin_mid_2DP >= bin_min_2DP_new[j], sd.bin_mid_2DP <= bin_max_2DP_new[j]))
    #     sd_2DP_new[j] = np.nansum(sd_2DP[ind_j] * sd.bin_dD_2DP.data[ind_j]) / np.nansum(sd.bin_dD_2DP.data[ind_j])
    sd_2DP_new = sd_2DP

    bins_CDP = np.array((bin_min_CDP, bin_mid_CDP, bin_max_CDP))
    bins_2DS = np.array((bin_min_2DS_new, bin_mid_2DS_new, bin_max_2DS_new))
    bins_2DP = np.array((sd.bin_min_2DP[1:], sd.bin_mid_2DP[1:], sd.bin_max_2DP[1:]))

    sd_CDP[sd_CDP == 0.] = np.nan
    sd_2DS_new[sd_2DS_new == 0.] = np.nan
    sd_2DP_new[sd_2DP_new == 0.] = np.nan

    # sd_CDP[np.logical_or(np.isnan(sd_CDP), sd_CDP == 0.)] = -9999.
    # sd_2DS_new[np.logical_or(np.isnan(sd_2DS_new), sd_2DS_new == 0.)] = -9999.
    # sd_2DP_new[np.logical_or(np.isnan(sd_2DP_new), sd_2DP_new == 0.)] = -9999.

    return sd_CDP, sd_2DS_new, sd_2DP_new, bins_CDP, bins_2DS, bins_2DP


def nev_corr(
    ka,
    iop,
    var = None,
    file = None
    ):

    t = np.array(ka.fields['HHMMSS']).astype(int)

    nev_ = ka.fields['nev_lwc']
    nev_tot_ = ka.fields['nev_twc']
    nev = nev_ + 0.
    nev_tot = nev_tot_ + 0.

    def _get_sheet(iop):
        if iop is 4:
            link = 'https://docs.google.com/spreadsheets/d/1QFxzhyLfFp0qMalODrILlS-EtIll6B3yuBSFMKHx6XM/export?gid=0&format=csv'
        if iop is 5:
            link = 'https://docs.google.com/spreadsheets/d/1V2CnGCfI-kMe5_nVQzW5Oo2pP9j1NW1mRMft97OvwSo/export?gid=0&format=csv'
        if iop is 6:
            link = 'https://docs.google.com/spreadsheets/d/1jBMiAZXulBUw7-YR_RQ_b7NpcPJgRbNk7_W_HkMU0Ow/export?gid=0&format=csv'
        
        df = pd.read_csv(link)

        return df

    if file is not None:
        df = pd.read_csv(file) 
    else:  
        df = _get_sheet(iop)

    num_corrections = int((len(df.columns) - 2) / 3)

    liq = np.where(df.var_flag == 'lwc')[0]
    tot = np.where(df.var_flag == 'twc')[0]

    for i in liq:
        for j in range(num_corrections):
            s = 'start_time' + str(j+1)
            e = 'end_time' + str(j+1)
            c = 'correction' + str(j+1)
               
            if np.isnan(df[s][i]):
                continue
            ind_liq = np.where(np.logical_and(t >= int(df[s][i]), t <= int(df[e][i])))

            if df[c][i] == 0:
                nev[ind_liq] = 0
            else:
                nev[ind_liq] = nev[ind_liq] + df[c][i]

    for i in tot:
        for j in range(num_corrections):
            s = 'start_time' + str(j+1)
            e = 'end_time' + str(j+1)
            c = 'correction' + str(j+1)

            if np.isnan(df[s][i]):
                continue
            ind_tot = np.where(np.logical_and(t >= int(df[s][i]), t <= int(df[e][i])))
            
            if df[c][i] == 0:
                nev_tot[ind_tot] = 0
            else:
                nev_tot[ind_tot] = nev_tot[ind_tot] + df[c][i]


    tot_gt = np.where(nev_tot > nev)
    nev[tot_gt] = nev[tot_gt] - (nev_tot[tot_gt]-nev[tot_gt])*0.05

    # nev_tot[nev_tot < nev] = nev[nev_tot < nev]

    nev_ice = nev_tot - nev

    if var is 'lwc':
        # print ('Liquid')
        return nev
    elif var is 'twc':
        # print ('Total')
        return nev_tot
    elif var is 'iwc':
        # print ('IT\'S ICE!')
        return nev_ice



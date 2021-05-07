'''Includes data corrections and for data from SNOWIE 2017'''

import numpy as np
import pandas as pd
# import sys
import uwagi

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
    file = None,
    test_flag = 0,
    qc_flag = 0
    ):

    '''
    Reads Nevzorov corrections from a table and outputs adjusted data.

    var:
        ice water = 'iwc'
        liquid water = 'lwc'
        total water = 'twc'

    file:
        if None, function will read Google sheet from _get_sheet()
        else, function will read user-supplied CSV

    test_flag:
        if 0, ice contamination is subtracted from lwc, twc is not allowed to be greater than lwc
        if 1, raw data from liquid and total

    qc_flag:
        if 0, function returns corrected Nevzorov data only
        if 1, function returns corrected Nevzorov data as 1st dimension and quality flag as 2nd dimension
        quality flags: 0=raw, 1=good, 2=bad (data labeled as 'bad' will be flagged as such but retained)
    '''

    t = np.array(ka.fields['HHMMSS']).astype(int)

    nev_ = ka.fields['nev_lwc']
    nev_tot_ = ka.fields['nev_twc']
    nev = nev_ + 0.
    nev_tot = nev_tot_ + 0.

    def _get_sheet(iop):
        if iop is 1:
            link = 'https://docs.google.com/spreadsheets/d/1c_OBUn973tWVQvMJB9QwACl9A3c3PvIfND45h2-FOGI/export?gid=0&format=csv'
        if iop is 2:
            link = 'https://docs.google.com/spreadsheets/d/1MN2lnpb6IQ_DOrM3SHnZYavGq2GsRnDx6kRQGzAcvbk/export?gid=0&format=csv'
        if iop is 3:
            link = 'https://docs.google.com/spreadsheets/d/1A1MQj0DHq7jFHjwt6JmjF_4padPwvFJMJ81ZBNs3ERM/export?gid=0&format=csv'
        if iop is 4:
            link = 'https://docs.google.com/spreadsheets/d/1QFxzhyLfFp0qMalODrILlS-EtIll6B3yuBSFMKHx6XM/export?gid=0&format=csv'
        if iop is 5:
            link = 'https://docs.google.com/spreadsheets/d/1V2CnGCfI-kMe5_nVQzW5Oo2pP9j1NW1mRMft97OvwSo/export?gid=0&format=csv'
        if iop is 6:
            link = 'https://docs.google.com/spreadsheets/d/1jBMiAZXulBUw7-YR_RQ_b7NpcPJgRbNk7_W_HkMU0Ow/export?gid=0&format=csv'
        if iop is 7:
            link = 'https://docs.google.com/spreadsheets/d/143vrgE9bgYGNeK7MTVYYT2anG-cmPJ9i004I7ZVu3Lk/export?gid=0&format=csv'
        if iop is 8:
            link = 'https://docs.google.com/spreadsheets/d/1hJkTQCO8T-gNalwH5T3n8mVBWADTijreLlbuT-99YaQ/export?gid=0&format=csv'
        if iop is 9:
            link = 'https://docs.google.com/spreadsheets/d/1zsLgYIEb0ZY0p2t1S262K-Joi8BWENbR5uOLfgfTn-A/export?gid=0&format=csv'
        if iop is 10:
            link = 'https://docs.google.com/spreadsheets/d/19Ah6nAxPK0TYdaKjp_N_jvSmHEVGDpuSJtiOVCjB3og/export?gid=0&format=csv'
        if iop is 11:
            link = 'https://docs.google.com/spreadsheets/d/1ym4VsjBhK9FmJ-Y6LoBNI4xj3ksOgWTE2VNvvyLn9l0/export?gid=0&format=csv'    
        if iop is 12:
            link = 'https://docs.google.com/spreadsheets/d/1HlWb4bUmejq4zO35M3pqbJIrvB8qYtv-YoN8kIagJdE/export?gid=0&format=csv'
        if iop is 13:
            link = 'https://docs.google.com/spreadsheets/d/1URz_ER6sLkZyGqgBzsWe0NA63siey0lup51416vntdo/export?gid=0&format=csv'
        if iop is 14:
            link = 'https://docs.google.com/spreadsheets/d/12U-Uwts6XkP-ZI9VPA3g9YL_IatNKVdxy9rTWR0q6bY/export?gid=0&format=csv'
        if iop is 15:
            link = 'https://docs.google.com/spreadsheets/d/1hPT0f3lUH6VCFOJmaQK1AZbhEUaeecAy_EhYX8b8MAs/export?gid=0&format=csv'
        if iop is 16:
            link = 'https://docs.google.com/spreadsheets/d/1Pwzk8kT33ZToDL-Ev4cGrxF2nSP_ppdj9pdeqoTtIG8/export?gid=0&format=csv'

        df = pd.read_csv(link)

        return df

    if file is not None:
        df = pd.read_csv(file) 
    else:  
        df = _get_sheet(iop)

    num_corrections = int((len(df.columns) - 2) / 3)

    liq = np.where(df.var_flag == 'liquid')[0]
    tot = np.where(df.var_flag == 'total')[0]

    if qc_flag == 1:
        print("ADDING QC FLAG OUTPUT AS SECOND ARRAY")
        nev_liq_flag = np.zeros_like(nev).astype(int)
        nev_tot_flag = np.zeros_like(nev_tot).astype(int)
        nev_ice_flag = np.zeros_like(nev_tot).astype(int)

        leg_times = np.array([])

        for i in range(1,20):
            try:
                start, end = uwagi.get_times(iop, leg=i)[0], uwagi.get_times(iop, leg=i)[1]

                p_start = np.where(np.array(ka.fields['HHMMSS']) == start)[0][0]
                p_end = np.where(np.array(ka.fields['HHMMSS']) == end)[0][0]
                time = np.array(ka.fields['HHMMSS'][p_start:p_end]).astype(int)

                leg_times = np.append(leg_times, time)
            except:
                print("Processed " + str(i-1) + ' legs for ' + var)
                break

        leg_ind = np.in1d(t, leg_times).nonzero()[0]
        nev_liq_flag[leg_ind] = 1
        nev_tot_flag[leg_ind] = 1
        nev_ice_flag[leg_ind] = 1
    
    else:
        pass

    for i in liq:
        for j in range(num_corrections):
            s = 'start_time' + str(j+1)
            e = 'end_time' + str(j+1)
            c = 'correction' + str(j+1)
               
            if np.isnan(df[s][i]):
                continue

            if df[s][i] > df[e][i]:
                ind_liq = np.append(np.where(np.logical_and(t >= int(df[s][i]), t > 0)), 
                    np.where(np.logical_and(t >= 0, t <= int(df[e][i]))))
            else:
                ind_liq = np.where(np.logical_and(t >= int(df[s][i]), t <= int(df[e][i])))

            if df[c][i] == -9999 and qc_flag == 1:
                nev_liq_flag[ind_liq] = 2
            elif df[c][i] == -9999 and qc_flag == 0:
                nev[ind_liq] = -9999
            else:
                nev[ind_liq] = nev[ind_liq] + df[c][i]            

    for i in tot:
        for j in range(num_corrections):
            s = 'start_time' + str(j+1)
            e = 'end_time' + str(j+1)
            c = 'correction' + str(j+1)

            if np.isnan(df[s][i]):
                continue

            if df[s][i] > df[e][i]:
                ind_tot = np.append(np.where(np.logical_and(t >= int(df[s][i]), t > 0)), 
                    np.where(np.logical_and(t >= 0, t <= int(df[e][i]))))
            else:
                ind_tot = np.where(np.logical_and(t >= int(df[s][i]), t <= int(df[e][i])))
            
            if df[c][i] == -9999 and qc_flag == 1:
                nev_tot_flag[ind_tot] = 2
            elif df[c][i] == -9999 and qc_flag == 0:
                nev_tot[ind_tot] = -9999
            else:
                nev_tot[ind_tot] = nev_tot[ind_tot] + df[c][i]

    if test_flag == 0:
        tot_gt = np.where(np.logical_and(nev_tot > nev, nev != 0))
        nev[tot_gt] = nev[tot_gt] - (nev_tot[tot_gt]-nev[tot_gt])*0.05
        nev_tot[nev_tot < nev] = nev[nev_tot < nev]
    elif test_flag == 1:
        print ('TEST MODE')

    nev_ice = nev_tot - nev

    if qc_flag == 1:
        nev_ice_flag[np.logical_or(nev_liq_flag == 2, nev_tot_flag == 2)] = 2
    else:
        pass

    if var is 'lwc':
        if qc_flag == 1:
            return nev, nev_liq_flag
        else:
            return nev
    elif var is 'twc':
        if qc_flag == 1:
            return nev_tot, nev_tot_flag
        else:
            return nev_tot
    elif var is 'iwc':
        if qc_flag == 1:
            return nev_ice, nev_ice_flag
        else:
            return nev_ice



'''Includes data corrections and adjustments for data from SNOWIE 2017'''

import numpy as np

'''
Adjust size distribution to set new bins
'''

def sd_corr(sd):

    bins_2DP = np.arange(100,20300,200)
    bins1 = np.arange(500,2100,200)
    bins2 = np.arange(2100,21100,1000)
    bins_2DP_re = np.append(bins1,bins2)
    bin_mid_2DP = (bins_2DP[1:] + bins_2DP[0:-1]) / 2
    bin_min_2DP_re = bins_2DP_re[0:-1]
    bin_max_2DP_re = bins_2DP_re[1:]
    bin_dD_2DP = bins_2DP[1:] - bins_2DP[0:-1]
    conc_2DP = conc_2DP[1:,:,:] * 1E-3
    conc_2DP = conc_2DP / bin_dD_2DP

    bin_mid_2DP_re = (bins_2DP_re[1:] + bins_2DP_re[0:-1]) / 2
    bin_dD_2DP_re = bins_2DP_re[1:] - bins_2DP_re[0:-1]
    sd_2DP_re = np.zeros_like(bin_dD_2DP_re)

    # times_info = sd_times.shape
    # n_times = len(sd_times) / 2

    ;CDP
    bin_mid_CDP = 0
    bin_dD_CDP = 0
    conc_CDP = 0

    ;2DS
    bin_mid_2DS = 0
    bin_dD_2DS = 0
    conc_2DS_both = 0

    i_both = np.where(sd.bin_mid_2DS > 40)

    bin_min_2DS = sd.bin_mid_2DS - sd.bin_dD_2DS / 2
    bin_max_2DS = sd.bin_mid_2DS + sd.bin_dD_2DS / 2
    bin_min_CDP = sd.bin_mid_CDP - sd.bin_dD_CDP / 2
    bin_max_CDP = sd.bin_mid_CDP + sd.bin_dD_CDP / 2
    bin_min_2DP = sd.bin_mid_2DP - sd.bin_dD_2DP / 2
    bin_max_2DP = sd.bin_mid_2DP + sd.bin_dD_2DP / 2 

    ind_min = np.arange(0,16)
    ind_min = np.append(ind_min, np.arange(16,48,2))
    ind_min = np.append(ind_min, np.arange(48,64,4))
    ind_min = np.append(ind_min, np.arange(64,96,8))
    ind_min = np.append(ind_min, np.arange(96,128,16))

    ind_max = np.arange(0,15)
    ind_max = np.append(ind_max, np.arange(15,47,2))
    ind_max = np.append(ind_max, np.arange(47,63,4))
    ind_max = np.append(ind_max, np.arange(63,95,8))
    ind_max = np.append(ind_max, np.arange(95,143,16))

    bin_min_2DS_re = bin_min_2DS[ind_min]
    bin_max_2DS_re = bin_max_2DS[ind_max]
    bin_dD_2DS_re = bin_max_2DS_re - bin_min_2DS_re
    bin_mid_2DS_re = np.round((bin_max_2DS_re + bin_min_2DS_re) / 2)
    sd_2DS_re = np.zeros_like(bin_mid_2DS_re)
    ind_re = np.where(bin_mid_2DS_re > 40)
    ind_driz_re = np.where(np.logical_and(bin_min_2DS_re >= 95, bin_max_2DS_re <= 295))
    ind_driz = np.where(np.logical_and(bin_mid_2DS >= 95, bin_mid_2DS <= 295)

    for i in (n_times-1):
        ind = np.where(np.logical_and(sd_hhmmss >= sd_times[0,i], sd_hhmmss < sd_times[1,i]))
        sd_2DS = np.mean(conc_2DS[:,ind], axis=2)
        sd_CDP = np.mean(conc_CDP[:,ind], axis=2)
        sd_2DP = np.mean(conc_2DP[:,ind], axis=2)









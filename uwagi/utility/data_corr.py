'''Includes data corrections and for data from SNOWIE 2017'''

import numpy as np

'''
Adjust size distribution to set new bins
'''

def sd_corr(
    sd,
    start_time,
    end_time,
    t_flag
    ):

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
        sd.dist_2DP[ind,:][sd.dist_2DP[ind,1:] == 0.] = np.nan

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
    # nev,
    # t
    # ):
    ka,
    iop
    ):

    t = np.array(ka.fields['HHMMSS']).astype(int)

    nev_ = ka.fields['nev_lwc']
    nev_tot_ = ka.fields['nev_twc']
    nev = nev_ + 0.
    nev_tot = nev_tot_ + 0.
# plt.plot(nev,nev_i)

    if iop is 4:

# LEG 1
        ind0 = np.where(np.logical_and(t >= 201540, t < 202845))
        nev[ind0] = 0.
        nev_tot[ind0] = 0.
        
        ind1 = np.where(np.logical_and(t >= 202845, t <= 203118))
        nev[ind1] = nev[ind1] - 0.02
        nev_tot[ind1] = nev_tot[ind1] - 0.02

# LEG 2
        ind0 = np.where(np.logical_and(t >= 203342, t <= 205020))
        nev[ind0] = nev[ind0] - 0.0183
        nev_tot[ind0] = nev_tot[ind0] - 0.0183

# LEG 4
        ind0 = np.where(np.logical_and(t >= 210728, t < 211830))
        nev[ind0] = nev[ind0] + 0.09
        nev_tot[ind0] = nev_tot[ind0] + 0.09

        ind1 = np.where(np.logical_and(t >= 211830, t <= 212432))
        nev[ind1] = nev[ind1] + 0.0094
        nev_tot[ind1] = nev_tot[ind1] + 0.0094

# LEG 5
        ind0 = np.where(np.logical_and(t >= 212710, t <= 213817))
        nev[ind0] = nev[ind0] - 0.0132
        nev_tot[ind0] = nev_tot[ind0] - 0.0132

    if iop is 5:
        
# LEG 1
        ind0 = np.where(np.logical_and(t >= 154002, t < 154830))
        nev[ind0] = nev[ind0] - 0.0132
        ind1 = np.where(np.logical_and(t >= 154830, t < 155125))
        nev[ind1] = nev[ind1] - 0.0092
        ind2 = np.where(np.logical_and(t >= 155125, t <= 155917))
        nev[ind2] = nev[ind2] - 0.0132

        # LEG 2
        ind3 = np.where(np.logical_and(t >= 160213, t < 161100))
        nev[ind3] = nev[ind3] - 0.016

        # LEG 4
        ind4 = np.where(np.logical_and(t >= 164550, t < 164830))
        nev[ind4] = nev[ind4] + 0.0106
        ind5 = np.where(np.logical_and(t >= 164830, t <= 165337))
        nev[ind5] = nev[ind5] + 0.0047

        # LEG 6
        ind6 = np.where(np.logical_and(t >= 171013, t <= 172303))
        nev[ind6] = nev[ind6] + 0.0133

        # LEG 7
        ind7 = np.where(np.logical_and(t >= 173300, t <= 173444))
        nev[ind7] = nev[ind7] + 0.056

        # LEG 8
        ind8 = np.where(np.logical_and(t >= 173758, t < 174000))
        nev[ind8] = nev[ind8] + 0.12
        ind9 = np.where(np.logical_and(t >= 174000, t < 174130))
        nev[ind9] = nev[ind9] + 0.14
        ind10 = np.where(np.logical_and(t >= 174130, t < 174200))
        nev[ind10] = nev[ind10] + 0.15
        ind11 = np.where(np.logical_and(t >= 174200, t < 174417))
        nev[ind11] = nev[ind11] + 0.18
        ind12 = np.where(np.logical_and(t >= 174417, t <= 174935))
        nev[ind12] = nev[ind12] + 0.08

        # LEG 9
        ind13 = np.where(np.logical_and(t >= 175157, t < 175348))
        nev[ind13] = nev[ind13] + 0.06

        # LEG 10
        ind14 = np.where(np.logical_and(t >= 181300, t <= 182151))
        nev[ind14] = nev[ind14] - 0.008


    tot_ind = np.where(nev_tot_ > nev)
    nev[tot_ind] = nev[tot_ind] - (nev_tot_[tot_ind]-nev[tot_ind])*0.05

    nev_tot_[nev_tot_ < nev] = nev[nev_tot_ < nev]


    return nev, nev_tot_













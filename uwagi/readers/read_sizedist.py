import numpy as np
from netCDF4 import Dataset
import datetime

'''
Reads NetCDF files from the University of Wyoming King Air Optical Array Probe
and returns an object containing the data.

Usage:
ka = uwagi.read_sd('filename')

Returns:
Object containing King Air OAP size distribution data
'''

def read_sd(filename):

    dist = _reader(filename)
    return dist

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        nc = Dataset(filename)

        self.time = nc.variables['time'][:]

        # 2DS
        self.bin_min_2DS = nc.variables['bin_min_2DS'][:]
        self.bin_max_2DS = nc.variables['bin_max_2DS'][:]
        self.bin_mid_2DS = nc.variables['bin_mid_2DS'][:]
        self.bin_dD_2DS = nc.variables['bin_dD_2DS'][:]
        self.dist_2DS_H = nc.variables['size_dist_2DS_H'][:]
        self.dist_2DS_V = nc.variables['size_dist_2DS_V'][:]
        self.conc_2DS_H = nc.variables['total_conc_2DS_H'][:]
        self.conc_2DS_V = nc.variables['total_conc_2DS_V'][:]

        # 2DP
        self.bin_min_2DP = nc.variables['bin_min_2DP'][:]
        self.bin_max_2DP = nc.variables['bin_max_2DP'][:]
        self.bin_mid_2DP = nc.variables['bin_mid_2DP'][:]
        self.bin_dD_2DP = nc.variables['bin_dD_2DP'][:]
        self.dist_2DP = nc.variables['size_dist_2DP'][:]
        self.conc_2DP = nc.variables['total_conc_2DP'][:]

        # CIP
        self.bin_min_CIP = nc.variables['bin_min_CIP'][:]
        self.bin_max_CIP = nc.variables['bin_max_CIP'][:]
        self.bin_mid_CIP = nc.variables['bin_mid_CIP'][:]
        self.bin_dD_CIP = nc.variables['bin_dD_CIP'][:]
        self.dist_CIP = nc.variables['size_dist_CIP'][:]
        self.conc_CIP = nc.variables['total_conc_CIP'][:]

        # CDP
        self.bin_min_CDP = nc.variables['bin_min_CDP'][:]
        self.bin_max_CDP = nc.variables['bin_max_CDP'][:]
        self.bin_mid_CDP = nc.variables['bin_mid_CDP'][:]
        self.bin_dD_CDP = nc.variables['bin_dD_CDP'][:]
        self.dist_CDP = nc.variables['size_dist_CDP'][:]
        self.conc_CDP = nc.variables['total_conc_CDP'][:]

        self._prep_data()
        # self._fix_time()

    def _prep_data(self):

        self.fields = {}

        self.fields["time"] = self.time[:]

        # 2DS
        if np.nansum(self.dist_2DS_H) is 0:
            h_2DS = 0
        else:
            h_2DS = 1
        if np.nansum(self.dist_2DS_V) is 0:
            v_2DS = 0
        else:
            v_2DS = 1

        channels = h_2DS + v_2DS

        self.dist_2DS_H[np.where(np.isfinite(self.dist_2DS_H) != 1)] = 0
        self.dist_2DS_V[np.where(np.isfinite(self.dist_2DS_V) != 1)] = 0

        self.ntot_2DS_H = np.nanmean(self.dist_2DS_H, axis=1)
        self.ntot_2DS_V = np.nanmean(self.dist_2DS_V, axis=1)

        if channels is 1:
            raise ValueError('One 2DS channel missing, using good channel only')
        if channels < 1:
            raise ValueError('!!!Both 2DS channels missing!!!')

        self.dist_2DS = (self.dist_2DS_H + self.dist_2DS_V) / channels

        self.fields["bin_min_2DS"] = self.bin_min_2DS
        self.fields["bin_max_2DS"] = self.bin_max_2DS
        self.fields["bin_mid_2DS"] = self.bin_min_2DS
        self.fields["bin_dD_2DS"] = self.bin_dD_2DS
        self.fields["size_dist_2DS_H"] = self.dist_2DS_H
        self.fields["size_dist_2DS_V"] = self.dist_2DS_V
        self.fields["size_dist_2DS"] = self.dist_2DS

        # 2DP
        self.fields["bin_min_2DP"] = self.bin_min_2DP
        self.fields["bin_max_2DP"] = self.bin_max_2DP
        self.fields["bin_mid_2DP"] = self.bin_min_2DP
        self.fields["bin_dD_2DP"] = self.bin_dD_2DP
        self.fields["size_dist_2DP"] = self.dist_2DP
        self.fields["conc_2DP"] = self.conc_2DP

        # CIP
        self.fields["bin_min_CIP"] = self.bin_min_CIP
        self.fields["bin_max_CIP"] = self.bin_max_CIP
        self.fields["bin_mid_CIP"] = self.bin_min_CIP
        self.fields["bin_dD_CIP"] = self.bin_dD_CIP
        self.fields["size_dist_CIP"] = self.dist_CIP
        self.fields["conc_CIP"] = self.conc_CIP

        # CDP
        self.fields["bin_min_CDP"] = self.bin_min_CDP
        self.fields["bin_max_CDP"] = self.bin_max_CDP
        self.fields["bin_mid_CDP"] = self.bin_min_CDP
        self.fields["bin_dD_CDP"] = self.bin_dD_CDP
        self.fields["size_dist_CDP"] = self.dist_CDP
        self.fields["conc_CDP"] = self.conc_CDP

'''
need different fix time function. time is in HHMMSS format without date or leading zeros.
'''

    # def _fix_time(self):

    #     date = self.filename[self.filename.find(2017),self.filename.find(2017)+8]

    #     start_time = datetime.datetime(2017,1,1,0,0,tzinfo=datetime.timezone.utc).timestamp()
    #     time_sec = self.time[:] + start_time
    #     self.fields['time'] = time_sec.astype('datetime64[s]')


# def ncvar_to_dict(ncvar):
    
#     d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
#     d["data"] = ncvar
#     if np.isscalar(d["data"]):
#         d["data"] = np.array(d["data"])
#         d["data"].shape = (1,)
#     return d


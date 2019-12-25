import numpy as np
from netCDF4 import Dataset
# from datetime import datetime

'''
Reads NetCDF files from the University of Wyoming King Air Optical Array Probe
and returns an object containing the data.

Usage:
ka = uwagi.read_sizedist('filename')

Returns:
Object containing King Air OAP size distribution data
'''

def read_sizedist(filename):

    dist = _reader(filename)
    return dist

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        nc = Dataset(filename)

        self.time = nc.variables['time']

        # 2DS
        self.min_2DS = nc.variables['bin_min_2DS']
        self.max_2DS = nc.variables['bin_max_2DS']
        self.mid_2DS = nc.variables['bin_mid_2DS']
        self.dD_2DS = nc.variables['bin_dD_2DS']
        self.dist_2DS_H = nc.variables['size_dist_2DS_H']
        self.dist_2DS_V = nc.variables['size_dist_2DS_V']

        # 2DP
        self.min_2DP = nc.variables['bin_min_2DP']
        self.max_2DP = nc.variables['bin_max_2DP']
        self.mid_2DP = nc.variables['bin_mid_2DP']
        self.dD_2DP = nc.variables['bin_dD_2DP']
        self.dist_2DP = nc.variables['size_dist_2DP']

        # CIP
        self.min_CIP = nc.variables['bin_min_CIP']
        self.max_CIP = nc.variables['bin_max_CIP']
        self.mid_CIP = nc.variables['bin_mid_CIP']
        self.dD_CIP = nc.variables['bin_dD_CIP']
        self.dist_CIP = nc.variables['size_dist_CIP']

        # CDP
        self.min_CDP = nc.variables['bin_min_CDP']
        self.max_CDP = nc.variables['bin_max_CDP']
        self.mid_CDP = nc.variables['bin_mid_CDP']
        self.dD_CDP = nc.variables['bin_dD_CDP']
        self.dist_CDP = nc.variables['size_dist_CDP']

        self._prep_data()

    def _prep_data(self):

        self.fields = {}

        self.fields["time"] = nc.variables['time'][:]

        # 2DS
        self.fields["bin_min_2DS"] = self.min_2DS[:]
        self.fields["bin_max_2DS"] = self.max_2DS[:]
        self.fields["bin_mid_2DS"] = self.min_2DS[:]
        self.fields["bin_dD_2DS"] = self.dD_2DS[:]
        self.fields["size_dist_2DS_H"] = self.dist_2DS_H[:]
        self.fields["size_dist_2DS_V"] = self.dist_2DS_V[:]

        # 2DP
        self.fields["bin_min_2DP"] = self.min_2DP[:]
        self.fields["bin_max_2DP"] = self.max_2DP[:]
        self.fields["bin_mid_2DP"] = self.min_2DP[:]
        self.fields["bin_dD_2DP"] = self.dD_2DP[:]
        self.fields["size_dist_2DP_H"] = self.dist_2DP[:]

        # CIP
        self.fields["bin_min_CIP"] = self.min_CIP[:]
        self.fields["bin_max_CIP"] = self.max_CIP[:]
        self.fields["bin_mid_CIP"] = self.min_CIP[:]
        self.fields["bin_dD_CIP"] = self.dD_CIP[:]
        self.fields["size_dist_CIP_H"] = self.dist_CIP[:]

        # CDP
        self.fields["bin_min_CDP"] = self.min_CDP[:]
        self.fields["bin_max_CDP"] = self.max_CDP[:]
        self.fields["bin_mid_CDP"] = self.min_CDP[:]
        self.fields["bin_dD_CDP"] = self.dD_CDP[:]
        self.fields["size_dist_CDP_H"] = self.dist_CDP[:]


# def ncvar_to_dict(ncvar):
    
#     d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
#     d["data"] = ncvar
#     if np.isscalar(d["data"]):
#         d["data"] = np.array(d["data"])
#         d["data"].shape = (1,)
#     return d


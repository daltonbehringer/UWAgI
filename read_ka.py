# import os
import numpy as np
from netCDF4 import Dataset

def KAReader(filename):

    ka = _reader(filename)
    return ka

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        # os.chdir('/Users/jbehrin1/Desktop/snowie_data/MP_files')

        nc = Dataset(filename)

        self.u = nc.variables['avux']
        self.v = nc.variables['avvy']
        self.ka_lat = nc.variables['GLAT']
        self.ka_lon = nc.variables['GLON']
        self.ka_time = nc.variables['TIME']
        self.ka_alt = nc.variables['avalt']
        self.wind_mag = nc.variables['avwmag']
        self.wind_dir = nc.variables['avwdir']
        self.roll = nc.variables['avroll']

        # self._read_file()
        self._prep_data()

    def _prep_data(self):

        self.fields["u_wind"] = ncvar_to_dict(self.u)
        self.fields["v_wind"] = ncvar_to_dict(self.v)
        self.fields["ka_lat"] = ncvar_to_dict(self.ka_lat)
        self.fields["ka_lon"] = ncvar_to_dict(self.ka_lon)
        self.fields["ka_time"] = ncvar_to_dict(self.ka_time)
        self.fields["ka_alt"] = ncvar_to_dict(self.ka_alt)
        self.fields["wind_mag"] = ncvar_to_dict(self.wind_mag)
        self.fields["wind_dir"] = ncvar_to_dict(self.wind_dir)
        self.fields["roll"] = ncvar_to_dict(self.roll)

def ncvar_to_dict(ncvar):
    
    d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
    d["data"] = ncvar
    if np.isscalar(d["data"]):
        d["data"] = np.array(d["data"])
        d["data"].shape = (1,)
    return d

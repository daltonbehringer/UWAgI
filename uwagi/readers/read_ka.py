import numpy as np
from netCDF4 import Dataset
from datetime import datetime

def read_ka(filename):

    ka = _reader(filename)
    return ka

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        nc = Dataset(filename)

        self.u = nc.variables['avux']
        self.v = nc.variables['avvy']
        self.lat = nc.variables['GLAT']
        self.lon = nc.variables['GLON']
        self.time = nc.variables['TIME']
        self.alt = nc.variables['avalt']
        self.wind_mag = nc.variables['avwmag']
        self.wind_dir = nc.variables['avwdir']
        self.roll = nc.variables['avroll']

        # self._read_file()
        self._prep_data()

    def _prep_data(self):

        self.fields = {}

        self.fields["u_wind"] = ncvar_to_dict(self.u)
        self.fields["v_wind"] = ncvar_to_dict(self.v)
        self.fields["lat"] = ncvar_to_dict(self.lat)
        self.fields["lon"] = ncvar_to_dict(self.lon)
        self.fields["time"] = ncvar_to_dict(self.time)
        self.fields["alt"] = ncvar_to_dict(self.alt)
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

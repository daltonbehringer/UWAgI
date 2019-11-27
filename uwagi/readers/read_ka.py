import numpy as np
from netCDF4 import Dataset
from datetime import datetime

'''
Reads NetCDF files from the University of Wyoming King Air
and returns an object containing the data.

Usage:
ka = uwagi.read_ka('filename')

Returns:
Object containing King Air Data
'''

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
        self.lwc100 = nc.variables['lwc100']
        self.nevlwc = nc.variables['nevlwc']
        self.nevtwc = nc.variables['nevtwc']
        self.cdplwc = nc.variables['cdplwc_NRB']
        self.cdpconc = nc.variables['cdpconc_NRB']
        self.pvmlwc = nc.variables['pvmlwc']
        self.temp = nc.variables['trf']
        self.dwpt = nc.variables['tdp70']
        self.airspeed = nc.variables['tas']

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
        self.fields["lwc100"] = ncvar_to_dict(self.lwc100)
        self.fields["nev_lwc"] = ncvar_to_dict(self.nevlwc)
        self.fields["nev_twc"] = ncvar_to_dict(self.nevtwc)
        self.fields["cdp_lwc"] = ncvar_to_dict(self.cdplwc_NRB)
        self.fields["cdp_conc"] = ncvar_to_dict(self.cdpconc_NRB)
        self.fields["lwc_pvm"] = ncvar_to_dict(self.pvmlwc)
        self.fields["temperature"] = ncvar_to_dict(self.trf)
        self.fields["dewpoint"] = ncvar_to_dict(self.tdp70)
        self.fields["airspeed"] = ncvar_to_dict(self.tas)

def ncvar_to_dict(ncvar):
    
    d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
    d["data"] = ncvar
    if np.isscalar(d["data"]):
        d["data"] = np.array(d["data"])
        d["data"].shape = (1,)
    return d

import numpy as np
from netCDF4 import Dataset
# from datetime import datetime

'''
Reads NetCDF files from the University of Wyoming King Air 2DS probe
and returns an object containing the data.

Usage:
ka = uwagi.read_2DS('filename')

Returns:
Object containing King Air 2DS data
'''

def read_2DS(filename):

    data = _reader(filename)
    return data

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        nc = Dataset(filename)

        self.time = nc.variables['Time'] # time for each particle (seconds since beginning of day)
        self.diameter = nc.variables['image_diam_minR'] # diameter for each particle (mm)
        self.reject = nc.variables['image_auto_reject'] # auto-reject variable - ascii characters - on github UW-UIOPS/img_processing/
        self.center = nc.variables['image_center_in'] # center of particle in sample volume. 1 = yes, 0 = no

        self._prep_data()

    def _prep_data(self):

        self.fields = {}

        self.fields["time"] = ncvar_to_dict(self.time)
        self.fields["particle_diameter"] = ncvar_to_dict(self.diameter)
        self.fields["image_auto_reject"] = ncvar_to_dict(self.reject)
        self.fields["particle_in_center"] = ncvar_to_dict(self.center)

def ncvar_to_dict(ncvar):
    
    d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
    d["data"] = ncvar
    if np.isscalar(d["data"]):
        d["data"] = np.array(d["data"])
        d["data"].shape = (1,)
    return d
import os
import pandas as pd
from netCDF4 import Dataset

def AircraftReader(filename):
    
    flight = _reader(filename)
    return flight

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        os.chdir('/Users/jbehrin1/Desktop/snowie_data/flight_info')

        data = pd.read_csv('20170119.csv')
        
        self.sa_time = data.Time
        self.sa_date = data.Date
        self.sa_lat = data.Latitude
        self.sa_lon = data.Longitude
        self.BIP = data.BIPcount
        self.EJ = data.EJcount
        self.sa_alt = data.Altitude_m

        os.chdir('/Users/jbehrin1/Desktop/snowie_data/MP_files')

        nc = Dataset('20170119a.c1.nc')

        self.u = nc.variables['avux'][:]
        self.v = nc.variables['avvy'][:]
        self.ka_lat = nc.variables['GLAT'][:]
        self.ka_lon = nc.variables['GLON'][:]
        self.ka_time = nc.variables['TIME'][:]
        self.ka_alt = nc.variables['avalt'][:]
        self.wind_mag = nc.variables['avwmag'][:]
        self.wind_dir = nc.variables['avwdir'][:]
        self.roll = nc.variables['avroll'][:]

        # self._read_file()
        self._prep_data()

    def var_to_dict(standard_name, data, units, long_name):
 
        d = {}
        d["data"] = data[:]
        d["units"] = units
        d["long_name"] = long_name
        d["standard_name"] = standard_name
        return d

    def ncvar_to_dict(ncvar):
    
        d = dict((k, getattr(ncvar, k)) for k in ncvar.ncattrs())
        d["data"] = ncvar[:]
        if np.isscalar(d["data"]):
            d["data"] = np.array(d["data"][:])
            d["data"].shape = (1,)
        return d

    def _prep_data(self):
        
        self.fields = {}

        self.fields["sa_time"] = var_to_dict(
            "Time", np.ma.array(self.sa_time), "HHMMSS", "Seeding Aircraft Time"
        )
        self.fields["sa_date"] = var_to_dict(
            "date", np.ma.array(self.sa_date), "M/D/Y", "Seeding Aircraft Date",
        )
        self.fields["sa_lat"] = var_to_dict(
            "lat", np.ma.array(self.sa_lat), " ", "Seeding Aircraft Latitude",
        )
        self.fields["sa_lon"] = var_to_dict(
            "lon", np.ma.array(self.sa_lon), " ", "Seeding Aircraft Longitude",
        )
        self.fields["BIP"] = var_to_dict(
            "Burn In Place", np.ma.array(self.BIP), " ", 
            "Burn In Place Flares (Active if n=[n-1]+1, burns for 4.5 min)",
        )
        self.fields["EJ"] = var_to_dict(
            "Ejectable", np.ma.array(self.EJ), " ", "Ejectable Flares (Active if n=[n-1]+1)",
        )
        self.fields["sa_alt"] = var_to_dict(
            "alt", np.ma.array(self.sa_alt), "m", "Seeding Aircraft Altitude",
        )
        
        self.fields["u_wind"] = ncvar_to_dict(self.u)
        self.fields["v_wind"] = ncvar_to_dict(self.v)
        self.fields["ka_lat"] = ncvar_to_dict(self.ka_lat)
        self.fields["ka_lon"] = ncvar_to_dict(self.ka_lon)
        self.fields["ka_time"] = ncvar_to_dict(self.ka_time)
        self.fields["ka_alt"] = ncvar_to_dict(self.ka_alt)
        self.fields["wind_mag"] = ncvar_to_dict(self.wind_mag)
        self.fields["wind_dir"] = ncvar_to_dict(self.wind_dir)
        self.fields["roll"] = ncvar_to_dict(self.roll)



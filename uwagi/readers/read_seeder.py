# import os
import numpy as np
import pandas as pd

def SeederReader(filename):
    
    seeder = _reader(filename)
    return seeder

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        # os.chdir('/Users/jbehrin1/Desktop/snowie_data/flight_info')

        data = pd.read_csv(filename)
        
        self.sa_time = data.Time
        self.sa_date = data.Date
        self.sa_lat = data.Latitude
        self.sa_lon = data.Longitude
        self.BIP = data.BIPcount
        self.EJ = data.EJcount
        self.sa_alt = data.Altitude_m

        self._prep_data()

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

def var_to_dict(standard_name, data, units, long_name):

    d = {}
    d["data"] = data[:]
    d["units"] = units
    d["long_name"] = long_name
    d["standard_name"] = standard_name
    return d



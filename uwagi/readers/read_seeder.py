import numpy as np
import pandas as pd

'''
Reads CSV files from the seeding aircraft 
during the SNOWIE campaign in 2017.

Usage:
seeder = uwagi.read_seeder('filename')

Returns:
Object containing seeding aircraft data
'''

def read_seeder(filename):
    
    seeder = _reader(filename)
    return seeder

class _reader(object):

    def __init__(self, filename):

        self.filename = filename

        data = pd.read_csv(filename)
        
        self.time = pd.Series([val.time() for val in pd.to_datetime(data.Time)])
        self.time = self.Time.str.replace(':', '').astype(int)

        self.date = pd.to_datetime(data.Date)
        self.lat = data.Latitude
        self.lon = data.Longitude
        self.BIP = data.BIPcount
        self.EJ = data.EJcount
        self.alt = data.Altitude_m

        self._prep_data()

    def _prep_data(self):
    
        self.fields = {}

        self.fields["time"] = var_to_dict(
            "Time", np.ma.array(self.time), "HHMMSS", "Seeding Aircraft Time"
        )
        self.fields["date"] = var_to_dict(
            "date", np.ma.array(self.date), "M/D/Y", "Seeding Aircraft Date",
        )
        self.fields["lat"] = var_to_dict(
            "lat", np.ma.array(self.lat), " ", "Seeding Aircraft Latitude",
        )
        self.fields["lon"] = var_to_dict(
            "lon", np.ma.array(self.lon), " ", "Seeding Aircraft Longitude",
        )
        self.fields["BIP"] = var_to_dict(
            "Burn In Place", np.ma.array(self.BIP), " ", 
            "Burn In Place Flares (Active if n=[n-1]+1, burns for 4.5 min)",
        )
        self.fields["EJ"] = var_to_dict(
            "Ejectable", np.ma.array(self.EJ), " ", "Ejectable Flares (Active if n=[n-1]+1)",
        )
        self.fields["alt"] = var_to_dict(
            "alt", np.ma.array(self.alt), "m", "Seeding Aircraft Altitude",
        )

def var_to_dict(standard_name, data, units, long_name):

    d = {}
    d["data"] = data[:]
    d["units"] = units
    d["long_name"] = long_name
    d["standard_name"] = standard_name
    return d



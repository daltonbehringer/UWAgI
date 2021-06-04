import uwagi
from netCDF4 import Dataset
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator

iop = 2

indir = '/Users/jbehrin1/Desktop/snowie_data/nevcorr/'
filename = uwagi.get_times(iop) + '.c1.nevcorr.nc'

nc = Dataset(indir + filename)

t = nc.variables['time'][:]

lwc_qual = nc.variables['lwcflag'][:]
twc_qual = nc.variables['twcflag'][:]
iwc_qual = nc.variables['iwcflag'][:]

lwc = nc.variables['nevlwc'][:]
twc = nc.variables['nevtwc'][:]
iwc = nc.variables['neviwc'][:]

fig = plt.figure(figsize=(10,4))
ax = plt.gca()

x_fmt = DateFormatter("%H%M%S")
ax.xaxis.set_major_formatter(x_fmt)
# ax.xaxis.set_major_locator(MinuteLocator(interval=30))
# ax.xaxis.set_minor_locator(MinuteLocator(interval=))

ax.plot(t, iwc_qual, 'r-', linewidth = .75, label = 'LWC Quality Flag')
# ax.plot(time, cdp, 'k:', linewidth = .75, label = 'CDP')
# ax.plot(time, nev_new, 'r-', linewidth = 1, label = 'Corr. Nevzorov')

ax.legend()

ax.grid(True)
ax.tick_params(axis='both', which='major', direction='in', grid_linestyle='-', grid_alpha=0.5,
    length=7, labelsize=12)
ax.tick_params(axis='both', which='minor', direction='in',length=4)

plt.show()

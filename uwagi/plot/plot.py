import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator

'''Lat/Lon for Packer John radar (SNOWIE 2017). Update as needed.'''
clat = 44.207692
clon = -116.0693

def plot(
    ka,
    var,
    clat,
    clon,
    xlims = None,
    ylims = None,
    tighten = True,
    vmin = None,
    vmax = None,
    cmap = None,
    ax = None,
    fig = None
    ):

    ax = parse_ax(ax)
    fig = parse_fig(fig)
    
    if vmin is None:
        vmin = np.nanmin(ka.fields[str(var)]["data"])
    if vmax is None:
        vmax = np.nanmax(ka.fields[str(var)]["data"])

    ### MAYBE MOVE THIS TO SEPARATE FUNC ###
    kdist = np.zeros((len(ka.time[:])))
    for i in range(len(kdist)-1):
        kdist[i] = 

    plt.plot(
        ka.time[:].filled(),
        ka.str(var)[:].filled(),
        vmin = vmin,
        vmax = vmax)



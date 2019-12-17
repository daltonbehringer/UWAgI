import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
import matplotlib.ticker as ticker
from ..utility.iop import which_data

'''Lat/Lon for Packer John radar (SNOWIE 2017). Update as needed.'''
# clat = 44.207692
# clon = -116.0693

'''Plot size distribution'''

# def plot_dist(
#     # placeholder
#     bin_min = None,
#     bin_max = None,
#     bin_mid = None,
#     bin_dd = None,
#     tighten = True,
#     ax = None,
#     fig = None
#     ):
    
#     ax = parse_ax(ax)
#     fig = parse_fig(fig)

#     if bin_min is None:
#         bin_min = [10,20,30,40,50,60,70,80,90,100,\
#         150,200,250,300,400,480,600,800,1000,1200,\
#         1400,1600,1800,2000,2200,2600,3000,3400,3800,\
#         4400,5000,6000,8000]
#     if bin_max is None:
#         bin_max = [20,30,40,50,60,70,80,90,100,150,200\
#         250,300,400,480,600,800,1000,1200,1400,1600,1800,\
#         2000,2200,2600,3000,3400,3800,4400,5000,6000,8000,10000]
#     if bin_mid is None:
#         bin_mid = [15,25,35,45,55,65,75,85,95,125,175,225,\
#         275,350,440,540,700,900,1100,1300,1500,1700,1900,\
#         2100,2400,2800,3200,3600,4100,4700,5500,7000,9000]
#     if bin_dd = None:
#         bin_dd = [10,10,10,10,10,10,10,10,10,50,50,50,50,\
#         100,80,120,200,200,200,200,200,200,200,200,400,400,\
#         400,400,600,600,1000,2000,2000]

'''Plot time-series'''

def plot_ts(
    ka,
    var,
    iop = None,
    leg = None,
    time_format = "%H%M",
    tz = None,
    x_min_tick_format = 'second',
    title = None,
    ax = None,
    fig = None,
    **kwargs
    ):

    '''
    Plots a time-series of a variable

    Usage: uwagi.plot.plot_ts(args)

    Arguments:
        ka = data object
        var = variable from data object
        iop = iop number
        leg = leg of the iop to plot

    Returns: matplotlib plot object
    '''

    ax = parse_ax(ax)
    fig = parse_fig(fig)

    start_time, end_time = which_data(iop, leg)[0], which_data(iop, leg)[1]

    x_fmt = DateFormatter(time_format, tz=tz)

    start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    ax.plot_date(ka.fields['time'][start:end], ka.fields[var]['data'][start:end], **kwargs)

    # ax.xaxis.set_major_formatter(dates.DateFormatter('%H%M'))

    ax.xaxis.set_major_formatter(x_fmt)
    ax.xaxis.set_major_locator(MinuteLocator(interval=2))
    
    # if x_min_tick_format == 'second':
    #     ax.xaxis.set_minor_locator(SecondLocator())
    # elif x_min_tick_format == 'minute':
    #     ax.xaxis.set_minor_locator(MinuteLocator())
    # elif x_min_tick_format == 'hour':
    #     ax.xaxis.set_minor_locator(HourLocator())
    # elif x_min_tick_format == 'day':
    #     ax.xaxis.set_minor_locator(DayLocator())

    if title is not None:
        ax.set_title(title)

    return fig, ax



def parse_ax(ax):
    """ Parse and return ax instance. """
    if ax is None:
        ax = plt.gca()
    return ax


def parse_fig(fig):
    """ Parse and return fig instance. """
    if fig is None:
        fig = plt.gcf()
    return fig




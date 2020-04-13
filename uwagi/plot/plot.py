import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors

from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
import matplotlib.ticker as ticker
from ..utility.iop import get_times
from ..utility.data_corr import sd_corr
from ..utility.var_labels import get_label

font = {'family': 'sans serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

'''Lat/Lon for Packer John radar (SNOWIE 2017). Update as needed.'''
# clat = 44.207692
# clon = -116.0693

'''Plot time-series'''

def plot_ts(
    ka,
    var,
    iop = None,
    leg = None,
    time_format = "%H%M",
    tz = None,
    x_min_tick_format = 'minute',
    title = None,
    y_label = None,
    ax = None,
    fig = None,
    tighten = True,
    ls = None,
    c = None,
    marker = None,
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

    fig = parse_fig(fig,10,4)
    ax = parse_ax(ax)

    start_time, end_time = get_times(iop, leg)[0], get_times(iop, leg)[1]

    x_fmt = DateFormatter(time_format)

    start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot_date(ka.fields['time'][start:end], ka.fields[var][start:end], ls=ls, c=c, marker=marker, **kwargs)

    ax.xaxis.set_major_formatter(x_fmt)
    ax.xaxis.set_major_locator(MinuteLocator(interval=2))
    
    if x_min_tick_format == 'second':
        ax.xaxis.set_minor_locator(SecondLocator())
    elif x_min_tick_format == 'minute':
        ax.xaxis.set_minor_locator(MinuteLocator())
    elif x_min_tick_format == 'hour':
        ax.xaxis.set_minor_locator(HourLocator())
    elif x_min_tick_format == 'day':
        ax.xaxis.set_minor_locator(DayLocator())

    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax.set_xlim([ka.fields['time'][start],ka.fields['time'][end]])

    ax.grid(True)
    ax.tick_params(axis='both', which='both', direction='in', grid_linestyle='--', grid_alpha=0.5)
    ax.set_xlabel('Time, UTC', fontdict=font)

    if y_label is None:
        ax.set_ylabel(get_label(var), fontdict=font)

    if title is None:
        ax.set_title(start_time[0:10]+' | IOP '+str(iop)+' | Leg '+str(leg), fontdict=font)
    elif title is not None:
        ax.set_title(title, fontdict=font)

    return fig, ax

'''Plot size distribution'''

def plot_sd(
    ka,
    # iop = None,
    # leg = None,
    start_time = None,
    end_time = None,
    title = None,
    y_label = None,
    ax = None,
    fig = None,
    tighten = True,
    ls = None,
    c = None,
    marker = None,
    **kwargs
    ):

    '''
    Plots a size distribution

    If not start time, entire leg is averaged

    Usage: uwagi.plot.plot_sd(args)

    Arguments:
        ka = data object
        iop = iop number

    Returns: matplotlib plot object
    '''

    fig = parse_fig(fig,6,6)
    ax = parse_ax(ax)

    # start_time, end_time = get_times(iop, leg)[0], get_times(iop, leg)[1]

    # start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    # end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    if start_time is None:
        start_time = int(ka.time[0])
    if end_time is None:
        end_time = int(ka.time[-1])

    # start_time = 151458
    # end_time = 183702

    sd_CDP, sd_2DS, sd_2DP, bins_CDP, bins_2DS, bins_2DP = sd_corr(ka, start_time, end_time)

    bins = np.append(bins_CDP, bins_2DS)
    bins = np.append(bins, bins_2DP)

    sd = np.append(sd_CDP, sd_2DS)
    sd = np.append(sd, sd_2DP)

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot(bins, sd, ls=ls, c=c, marker=marker, **kwargs)

    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax.set_xscale('log')
    ax.set_xlim([1E1, 1E4])
    ax.set_yscale('log')
    ax.set_ylim([1E-10, 1E2])

    ax.tick_params(axis='both', which='both', direction='in', length = 7)
    
    ax.set_xlabel(r'Particle Diameter, $\mu m$')
    ax.set_ylabel(r'# $cm^{-3}\/\mu m^{-1}$')

    if title is None:
        ax.set_title(str(start_time) + ' - ' + str(end_time), fontdict=font)
    elif title is not None:
        ax.set_title(title, fontdict=font)

    return fig, ax

def parse_fig(fig,x,y):
    """ Parse and return fig instance. """
    if fig is None:
        fig = plt.figure(figsize=(x,y))
    return fig

def parse_ax(ax):
    """ Parse and return ax instance. """
    if ax is None:
        ax = plt.gca()
    return ax


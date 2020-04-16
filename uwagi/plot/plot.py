import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors

from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
import matplotlib.ticker as ticker
from ..utility.iop import get_times
from ..readers.read_ka import read_ka
from ..readers.read_sizedist import read_sd
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
    var,
    iop = None,
    start = None,
    end = None,
    leg = None,
    file_loc = None,
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

    Usage: uwagi.plot_ts(args)

    Arguments:
        ka = data object
        var = variable from data object
        iop = iop number
        leg = leg of the iop to plot

    Returns: matplotlib plot object
    '''

    # if start is not None and end is not None and leg is not None:
    #     raise ValueError('***Use either start/end or entire leg***')
    print(start)

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Plotting data from entire leg '+str(leg)+' period.')
        start_time, end_time = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    if start is not None and end is not None and leg is None:
        start_time, end_time = get_times(iop, start=start, end=end)[0], get_times(iop, start=start, end=end)[1]

    filename = get_times(iop)+'.c1.nc'

    if file_loc is not None:
        ka = read_ka(file_loc+filename)
    else:
        ka = read_ka(filename)

    fig = parse_fig(fig,10,4)
    ax = parse_ax(ax)

    x_fmt = DateFormatter(time_format)

    p_start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    p_end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    t = ka.fields['time'][p_start:p_end]
    y = ka.fields[var][p_start:p_end]

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot_date(t, y, ls=ls, c=c, marker=marker, **kwargs)

    variance = np.round(np.nanvar(y), decimals=2)
    stdev = np.round(np.nanstd(y), decimals=2)
    mean = np.round(np.nanmean(y), decimals=2)

    ax.xaxis.set_major_formatter(x_fmt)
    ax.xaxis.set_major_locator(MinuteLocator(interval=2))
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.set_xlabel('Time, UTC', fontdict=font)
    
    if x_min_tick_format == 'second':
        ax.xaxis.set_minor_locator(SecondLocator())
    elif x_min_tick_format == 'minute':
        ax.xaxis.set_minor_locator(MinuteLocator())
    elif x_min_tick_format == 'hour':
        ax.xaxis.set_minor_locator(HourLocator())
    elif x_min_tick_format == 'day':
        ax.xaxis.set_minor_locator(DayLocator())

    ax.set_xlim([ka.fields['time'][p_start],ka.fields['time'][p_end]])

    ax.grid(True)
    ax.tick_params(axis='both', which='major', direction='in', grid_linestyle='--', grid_alpha=0.5,
        length=7, labelsize=12)
    ax.tick_params(axis='both', which='minor', direction='in',length=4)

    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax.set_ylim(ymin = -0.01)

    if y_label is None:
        ax.set_ylabel(get_label(var), fontdict=font)

    if title is None and leg is not None:
        ax.set_title(start_time[0:10]+' | IOP '+str(iop)+' | Leg '+str(leg)+'\n'
            +'Mean: '+str(mean)+' StDev: '+str(stdev)+' Var: '+str(variance), fontdict=font)
    elif title is None and leg is None:
        ax.set_title(start_time[0:10]+' | IOP '+str(iop)+' | '+str(start)+' - '+str(end)+'\n'
            +'Mean: '+str(mean)+' StDev: '+str(stdev)+' Var: '+str(variance), fontdict=font)
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

    Usage: uwagi.plot_sd(args)

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

    bins = np.append(bins_CDP[1], bins_2DS[1])
    bins = np.append(bins, bins_2DP[1])

    sd = np.append(sd_CDP, sd_2DS)
    sd = np.append(sd, sd_2DP)

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot(bins, sd, ls=ls, c=c, marker=marker, **kwargs)

    ax.set_xscale('log')
    ax.set_xlim([1E0, 1E4])
    ax.set_yscale('log')
    ax.set_ylim([1E-10, 1E2])

    ax.tick_params(axis='both', which='both', direction='in', length = 7, grid_linestyle='--', grid_alpha=0.5)
    ax.yaxis.set_major_locator(ticker.LogLocator(base=10, numticks=7))
    
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


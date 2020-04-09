import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors

from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
import matplotlib.ticker as ticker
from ..utility.iop import get_times
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
    var,
    iop = None,
    leg = None,
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

    Usage: uwagi.plot.plot_sd(args)

    Arguments:
        ka = data object
        var = which probe to get size dist from, or average ('mean')
        iop = iop number
        leg = leg of the iop to plot

    Returns: matplotlib plot object
    '''

    fig = parse_fig(fig,6,6)
    ax = parse_ax(ax)

    # start_time, end_time = get_times(iop, leg)[0], get_times(iop, leg)[1]

    # start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    # end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    print(var)

    if var is '2ds' or '2DS':
        dist = (ka.dist_2DS_H * ka.dist_2DS_V) / 2
        bins = ka.mid_2DS
        dist[dist == 0.] = np.nan
        sd = np.nanmean(dist, axis=0)
    # if var is '2dp' or '2DP':
    #     dist = ka.dist_2DP
    #     bins = ka.mid_2DP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)
    #     print('2DP')
    # if var is 'cdp' or 'CDP':
    #     dist = ka.dist_CDP
    #     bins = ka.mid_CDP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)
    # if var is 'cip' or 'CIP':
    #     dist = ka.dist_CIP
    #     bins = ka.mid_CIP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot(bins, sd, ls=ls, c=c, marker=marker, **kwargs)

    # ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax.set_xscale('log')
    ax.set_xlim([1E1, 1E4])
    ax.set_yscale('log')
    ax.set_ylim([1E-10, 1E2])

    ax.tick_params(axis='both', which='both', direction='in', length = 7)
    
    ax.set_xlabel(r'Particle Diameter, $\mu m$')
    ax.set_ylabel(r'# $cm^{-3}\/\mu m^{-1}$')

    # if title is None:
    #     ax.set_title(start_time[0:10]+' | IOP '+str(iop)+' | Leg '+str(leg), fontdict=font)
    # elif title is not None:
    #     ax.set_title(title, fontdict=font)

    return fig, ax

'''Plot size distribution time-series'''

def plot_sd_hov(
    ka,
    var,
    iop = None,
    leg = None,
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
    Plots a size distribution using a Hovmoller-type plot

    Usage: uwagi.plot.plot_sd_hov(args)

    Arguments:
        ka = data object
        var = which probe to get size dist from, or average ('mean')
        iop = iop number
        leg = leg of the iop to plot

    Returns: matplotlib plot object
    '''

    fig = parse_fig(fig,10,4)
    ax = parse_ax(ax)

    # start_time, end_time = get_times(iop, leg)[0], get_times(iop, leg)[1]

    # start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    # end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    time = ka.time

    if var is '2ds' or '2DS':
        sd = (ka.dist_2DS_H * ka.dist_2DS_V) / 2
        bins = ka.mid_2DS
        sd[sd == 0.] = np.nan
    # if var is '2dp' or '2DP':
    #     dist = ka.dist_2DP
    #     bins = ka.mid_2DP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)
    #     print('2DP')
    # if var is 'cdp' or 'CDP':
    #     dist = ka.dist_CDP
    #     bins = ka.mid_CDP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)
    # if var is 'cip' or 'CIP':
    #     dist = ka.dist_CIP
    #     bins = ka.mid_CIP
    #     dist[dist == 0.] = np.nan
    #     sd = np.nanmean(dist, axis=0)

    y, x = np.meshgrid(bins, time)

    cmap = plt.get_cmap('plasma')

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.set_yscale('log')
    ax.set_ylim([1E1, 1E4])

    ax.tick_params(axis='both', which='both', direction='in', length = 7)
    
    ax.set_xlabel(r'Time, UTC')
    ax.set_ylabel(r'Particle Diameter, $\mu m$')

    vmin, vmax = 1E-8, 1E0

    sd_plot = plt.pcolormesh(x, y, sd, 
        norm=colors.LogNorm(vmin=vmin,vmax=vmax), cmap=cmap)

    fig.colorbar(sd_plot, ax=ax)

    # if title is None:
    #     ax.set_title(start_time[0:10]+' | IOP '+str(iop)+' | Leg '+str(leg), fontdict=font)
    # elif title is not None:
    #     ax.set_title(title, fontdict=font)

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


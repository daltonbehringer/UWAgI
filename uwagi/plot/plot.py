import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors

from matplotlib import rc
from matplotlib.dates import DateFormatter
from matplotlib.dates import SecondLocator, MinuteLocator, HourLocator, DayLocator
import matplotlib.ticker as ticker
from ..utility.iop import get_times
from ..readers.read_ka import read_ka
from ..readers.read_sizedist import read_sd
from ..utility.data_corr import sd_corr
from ..utility.data_corr import nev_corr
from ..utility.var_labels import get_label
from ..utility.distance import dist

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'dejavusans'
matplotlib.rc('font', family='sans serif')

font = {'family': 'sans serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
labelsize = 16

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
    indir = None,
    time_format = "%H%M%S",
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
        var = variable to plot
        iop = iop number
        leg = leg of the iop to plot
        start = start time of plot
        end = end time of plot

    Returns: matplotlib plot object
    '''

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Plotting data from entire leg '+str(leg)+' period.')
        start, end = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    filename = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            ka = read_ka(indir+filename)
        else:
            ka = read_ka(indir+'/'+filename)
    else:
        ka = read_ka(filename)

    if start is None:
        start = ka.fields['HHMMSS'][0]
    if end is None:
        end = ka.fields['HHMMSS'][-1]

    fig = parse_fig(fig,10,4)
    ax = parse_ax(ax)

    x_fmt = DateFormatter(time_format)

    p_start = np.where(np.array(ka.fields['HHMMSS']) == str(start))[0][0]
    p_end = np.where(np.array(ka.fields['HHMMSS']) == str(end))[0][0]

    t = ka.fields['time'][p_start:p_end]
    y = ka.fields[var][p_start:p_end]

    if ls is None:
        ls = '-'
    if c is None:
        c = 'k'

    ax.plot_date(t, y, ls=ls, c=c, marker=marker, **kwargs)

    variance = np.round(np.nanvar(y), decimals=3)
    stdev = np.round(np.nanstd(y), decimals=3)
    mean = np.round(np.nanmean(y), decimals=3)

    ax.xaxis.set_major_formatter(x_fmt)
    ax.xaxis.set_major_locator(MinuteLocator(interval=5))
    # ax.xaxis.set_major_locator(SecondLocator(interval=20))
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
        length=7, labelsize=labelsize)
    ax.tick_params(axis='both', which='minor', direction='in',length=4)

    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))

    if y_label is None:
        ax.set_ylabel(get_label(var), fontdict=font)

    if title is None and leg is not None:
        ax.set_title('IOP '+str(iop)+' | Leg '+str(leg)+'\n'
            +'Mean: '+str(mean)+' StDev: '+str(stdev)+' Var: '+str(variance), fontdict=font)
    elif title is None and leg is None:
        ax.set_title('IOP '+str(iop)+' | '+str(start)+' - '+str(end)+'\n'
            +'Mean: '+str(mean)+' StDev: '+str(stdev)+' Var: '+str(variance), fontdict=font)
    elif title is not None:
        ax.set_title(title, fontdict=font)

    return fig, ax

'''Plot size distribution'''

def plot_sd(
    iop,
    leg = None,
    start = None,
    end = None,
    indir = None,
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

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Gathering data from entire leg '+str(leg)+' period.')
        start, end = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]
    
    filename = get_times(iop)+'.SD.cdf'

    if indir is not None:
        if indir[-1] is '/':
            sd = read_sd(indir+filename)
        else:
            sd = read_sd(indir+'/'+filename)
    else:
        sd = read_sd(filename)

    # if start is None:
    #     start = int(sd.time[0])
    # if end is None:
    #     end = int(sd.time[-1])

    fig = parse_fig(fig,6,6)
    ax = parse_ax(ax)

    # start_time, end_time = get_times(iop, leg)[0], get_times(iop, leg)[1]

    # start = np.where(ka.fields['time'] == np.datetime64(start_time))[0][0]
    # end = np.where(ka.fields['time'] == np.datetime64(end_time))[0][0]

    # start_time = 151458
    # end_time = 183702

    sd_CDP, sd_2DS, sd_2DP, bins_CDP, bins_2DS, bins_2DP = sd_corr(sd, int(start), int(end), 0)
    print (start)

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

    ax.tick_params(axis='both', which='both', direction='in', length = 7, grid_linestyle='--', grid_alpha=0.5, labelsize=labelsize)
    ax.yaxis.set_major_locator(ticker.LogLocator(base=10, numticks=7))
    
    ax.set_xlabel(r'Particle Diameter, $\mu m$', fontdict=font)
    ax.set_ylabel(r'# $cm^{-3}\/\mu m^{-1}$', fontdict=font)

    if title is None and leg is not None:
        ax.set_title('IOP '+str(iop)+' | Leg '+str(leg), fontdict=font)
    elif title is None and leg is None:
        ax.set_title('IOP '+str(iop)+' | '+str(start)+' - '+str(end), fontdict=font)
    elif title is not None:
        ax.set_title(title, fontdict=font)

    return fig, ax


'''Plot size dist hovmoller'''
def plot_sd_hov(
    iop,
    leg = None,
    start = None,
    end = None,
    indir = None,
    time_format = "%H%M%S",
    x_axis = None,
    second_var = None,
    cmap = None,
    vmin = None,
    vmax = None,
    title = None,
    y_label = None,
    ax = None,
    fig = None,
    tighten = True,
    **kwargs
    ):

    '''
    Plots a size distribution Hovmoller over time or space.

    If not start time, entire leg is averaged

    Usage: uwagi.plot_sd_hov(args)

    Arguments:
        ka = data object
        iop = iop number

    Returns: matplotlib plot object
    '''

    if start is None and end is None and leg is None:
        raise ValueError('***Need either start/end or leg number***')
    
    if start is None and end is None and leg is not None:
        print('Gathering data from entire leg '+str(leg)+' period.')
        start, end = int(get_times(iop, leg=leg)[0]), int(get_times(iop, leg=leg)[1])
    
    # if start is not None and end is not None and leg is None:
    #     start_time, end_time = get_times(iop, start=start, end=end)[0], get_times(iop, start=start, end=end)[1

    filename = get_times(iop)+'.SD.cdf'
    filename_ka = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            sd = read_sd(indir+filename)
            ka = read_ka(indir+filename_ka)
        else:
            sd = read_sd(indir+'/'+filename)
            ka = read_ka(indir+'/'+filename_ka)
    else:
        sd = read_sd(filename)
        ka = read_ka(filename_ka)

    # if start is None:
    #     start = int(sd.time[0])
    # if end is None:
    #     end = int(sd.time[-1])

    fig = parse_fig(fig,10,4)
    ax = parse_ax(ax)

    p_start = np.where(sd.time == start)[0][0]
    p_end = np.where(sd.time == end)[0][0]

    t = sd.time[p_start:p_end]#.astype(int)
    t_sec = np.arange(0,len(t))

    sd_CDP = np.zeros((27,len(t)))
    sd_2DS = np.zeros((30,len(t)))
    sd_2DP = np.zeros((18,len(t)))

    for i in range(len(t)):
        sd_CDP[:,i], sd_2DS[:,i], sd_2DP[:,i], bins_CDP, bins_2DS, bins_2DP = sd_corr(sd, t[i], t[i], 1)

    sd = np.append(sd_CDP, sd_2DS, axis=0)
    sd = np.append(sd, sd_2DP, axis=0)

    bin_min = np.append(bins_CDP[0], bins_2DS[0])
    bin_min = np.append(bin_min, bins_2DP[0])

    bin_mid = np.append(bins_CDP[1], bins_2DS[1])
    bin_mid = np.append(bin_mid, bins_2DP[1])

    bin_max = np.append(bins_CDP[2], bins_2DS[2])
    bin_max = np.append(bin_max, bins_2DP[2])

    if cmap is None:
        cmap = plt.get_cmap('plasma')

    if vmin is None:
        vmin = 1E-10
    if vmax is None:
        vmax = 1E2

    if x_axis is None or x_axis is 'seconds':
        p = ax.pcolormesh(t_sec, bin_mid, sd, norm=colors.LogNorm(), cmap=cmap, vmin=vmin, vmax=vmax)
        ax.set_xlabel('Seconds from start', fontdict=font)
        ax.set_xlim([t_sec[0],t_sec[-1]])
    elif x_axis is 'time':
        x_fmt = DateFormatter(time_format)
        p = ax.pcolormesh(t, bin_mid, sd, norm=colors.LogNorm(), cmap=cmap, vmin=vmin, vmax=vmax)
        ax.set_xlabel('Time, UTC', fontdict=font)
        ax.set_xlim([t[0],t[-1]])
    elif x_axis is 'space':
        lats = ka.fields['lat']
        lons = ka.fields['lon']
        d = dist(lats, lons)[p_start:p_end]
        p = ax.pcolormesh(d, bin_mid, sd, norm=colors.LogNorm(), cmap=cmap, vmin=vmin, vmax=vmax)
        ax.set_xlabel('Distance from PJ (km)', fontdict=font)
        ax.set_xlim([np.min(d),np.max(d)])
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
        
    ax.set_yscale('log')
    ax.set_ylim([2.5E0,1E4])
    ax.grid(True)
    ax.tick_params(axis='both', which='major', direction='in', length=7, grid_linestyle='--', grid_alpha=0.5, labelsize=labelsize)
    ax.tick_params(axis='both', which='minor', direction='in', length=4)

    ax.set_ylabel('Particle Diameter (\u03bcm)', fontdict=font)

    if second_var is None:
        cbar = plt.colorbar(p, cmap=cmap)
        cbar.ax.tick_params(labelsize=12)
        cbar.set_label('# cm$^{-3}\/$'+'\u03bc'+'m$^{-1}$', fontdict=font)
    else:
        cbar = plt.colorbar(p, cmap=cmap, pad=0.12)
        cbar.ax.tick_params(labelsize=12)
        cbar.set_label('# cm$^{-3}\/$'+'\u03bc'+'m$^{-1}$', fontdict=font)
        ax2 = ax.twinx()
        
        # if second_var is 'nev_lwc':
        #     y2 = nev_corr(ka, iop)[p_start:p_end]
        # else:
        #     y2 = ka.fields[second_var][p_start:p_end]
        
        y2 = nev_corr(ka, iop, var='lwc')[p_start:p_end]
        y3 = nev_corr(ka, iop, var='twc')[p_start:p_end]

        ax2.plot(d, y2, ls='-', c='k', linewidth=0.6, label='Liquid', **kwargs)
        ax2.plot(d, y3, ls='-', c='b', linewidth=0.6, label='Total', **kwargs)
        ax2.set_ylim(ymin=0)
        ax2.set_ylabel(get_label('water_content'), fontdict=font)
        ax2.legend(loc=2, fontsize=12)
        ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.025))
        ax2.tick_params(axis='y', which='major', direction='in', length=7, grid_linestyle='--', grid_alpha=0.5, labelsize=labelsize)
        ax2.tick_params(axis='y', which='minor', direction='in', length=4)

    if title is None and leg is not None:
        ax.set_title('IOP '+str(iop)+' | '+str(start)+' - '+str(end)+' (Leg '+str(leg)+')', fontdict=font)
    elif title is None and leg is None:
        ax.set_title('IOP '+str(iop)+' | '+str(start)+' - '+str(end), fontdict=font)
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














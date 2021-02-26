import numpy as np
from ..utility.iop import get_times
from ..utility.distance import dist
from ..readers.read_ka import read_ka

'''
Contains functions to get index of points inside or outside of manually identified plumes.
In-plume times use -10 dBZ threshold unless only 0 dBZ is available. Out-of-plume uses 
user-specified distance downwind of downwind-most plume.
'''

def get_plume(
    iop = None,
    leg = None,
    plume = None,
    indir = None
    ):

    if iop is None or leg is None:
        raise ValueError('Function requires IOP and leg number.')

    start, end, ka = get_times(iop=iop, leg=leg)[0], get_times(iop=iop, leg=leg)[1], get_times(iop=iop, leg=leg)[2]

    filename_ka = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            ka = read_ka(indir+filename_ka)
        else:
            ka = read_ka(indir+'/'+filename_ka)
    else:
        ka = read_ka(filename)

    p_start = np.where(np.array(ka.fields['HHMMSS']) == str(start))[0][0]
    p_end = np.where(np.array(ka.fields['HHMMSS']) == str(end))[0][0]

    t = np.array(ka.fields['HHMMSS']).astype(int)[p_start:p_end]

    '''
    IOP 5
    '''

    if iop is 5:

        if leg is 4:
            p_ind = np.where(np.logical_and(t >= 165053, t <= 165054))
            
            if plume is not None:
                print ('Leg ' + str(leg) + ' only contains one plume.')

        elif leg is 5:
            p_ind = np.where(np.logical_and(t >= 165749, t <= 165803))

            if plume is not None:
                print ('Leg ' + str(leg) + ' only contains one plume.')

        elif leg is 6:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 171814, t <= 171847))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 171728, t <= 171738))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 171814, t <= 171847))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 171728, t <= 171738)))

        elif leg is 7:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 172839, t <= 172926))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 172951, t <= 173015))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 172839, t <= 172926))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 172951, t <= 173015)))

        elif leg is 8:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 174121, t <= 174210))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 174050, t <= 174111))
            
            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 174121, t <= 174210))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 174050, t <= 174111)))
        
        elif leg is 9:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 175850, t <= 175936))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 175951, t <= 180029))
            
            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 175850, t <= 175936))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 175951, t <= 180029)))

        elif leg is 10:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 180410, t <= 180429))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 180438, t <= 180458))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 180410, t <= 180429))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 180438, t <= 180458)))

        else:
            print ('**NO SEEDING PLUME**')

    '''
    IOP 8
    '''

    if iop is 8:

        if leg is 4:
            print ('NO PLUMES IDENTIFIED')

        elif leg is 5:
            if plume is 'A':
                p_ind = np.where(np.logical_and(t >= 231318, t <= 221330))

            if plume is 'B':
                p_ind = np.where(np.logical_and(t >= 221159, t <= 221208))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 231318, t <= 221330))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 221159, t <= 221208)))

        elif leg is 6:
            p_ind = np.where(np.logical_and(t >= 222512, t <= 222535))

        elif leg is 7:
            p_ind = np.where(np.logical_and(t >= 224400, t <= 224410))

        elif leg is 8:
            if plume is 'C':
                p_ind = np.where(np.logical_and(t >= 230134, t <= 230144))

            if plume is 'D':
                p_ind = np.where(np.logical_and(t >= 230415, t <= 230417))

            if plume is 'E':
                p_ind = np.where(np.logical_and(t >= 230618, t <= 230625))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 230134, t <= 230144))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 230415, t <= 230417)))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 230618, t <= 230625)))
        
        elif leg is 9:
            p_ind = np.where(np.logical_and(t >= 232005, t <= 232015))

        elif leg is 10:
            if plume is 'C':
                p_ind = np.where(np.logical_and(t >= 232936, t <= 232957))

            if plume is 'E':
                p_ind = np.where(np.logical_and(t >= 233427, t <= 233452))

            if plume is 'all' or plume is 'ALL' or plume is None:
                p_ind = np.where(np.logical_and(t >= 232936, t <= 232957))
                p_ind = np.append(p_ind, np.where(np.logical_and(t >= 233427, t <= 233452)))

        elif leg is 11:
            print ('NO PLUMES IDENTIFIED')
        
        elif leg is 12:
            print ('NO PLUMES IDENTIFIED')

        else:
            print ('**NO SEEDING PLUME**')

    return p_ind


def get_out_plume(
    iop = None,
    leg = None,
    dist_out = None,
    indir = None
    ):

    start, end = get_times(iop=iop, leg=leg)[0], get_times(iop=iop, leg=leg)[1], get_times(iop=iop, leg=leg)[2]

    filename = get_times(iop)+'.c1.nc'

    if indir is not None:
        if indir[-1] is '/':
            ka = read_ka(indir+filename_ka)
        else:
            ka = read_ka(indir+'/'+filename_ka)
    else:
        ka = read_ka(filename)

    p_start = np.where(np.array(ka.fields['HHMMSS']) == str(start))[0][0]
    p_end = np.where(np.array(ka.fields['HHMMSS']) == str(end))[0][0]

    t = np.array(ka.fields['HHMMSS']).astype(int)[p_start:p_end]

    '''
    IOP 5
    '''

    if iop is 5:

        lats = ka.fields['lat']
        lons = ka.fields['lon']
        d = dist(lats, lons)[p_start:p_end]

        if leg is 4:
            end_plume_ind = np.where(t == 165053)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 5:
            end_plume_ind = np.where(t == 165803)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 6:
            end_plume_ind = np.where(t == 171728)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))
        
        if leg is 7:
            end_plume_ind = np.where(t == 173015)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))
        
        if leg is 8:
            end_plume_ind = np.where(t == 174050)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 9:
            end_plume_ind = np.where(t == 180029)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 10:
            end_plume_ind = np.where(t == 180438)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

    '''
    IOP 8
    '''

    if iop is 8:

        lats = ka.fields['lat']
        lons = ka.fields['lon']
        d = dist(lats, lons)[p_start:p_end]

        if leg is 5:
            end_plume_ind = np.where(t == 221330)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 6:
            end_plume_ind = np.where(t == 222512)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 7:
            end_plume_ind = np.where(t == 224410)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 8:
            end_plume_ind = np.where(t == 230134)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 9:
            end_plume_ind = np.where(t == 232015)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 10:
            end_plume_ind = np.where(t == 232936)[0][0]
            end_plume_d = d[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))


    return out_plume[0]   


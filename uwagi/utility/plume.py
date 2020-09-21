import numpy as np
from ..utility.iop import get_times
from ..utility.distance import dist


def get_plume(
    ka,
    iop,
    leg

    ):

    t = np.array(ka.fields['HHMMSS']).astype(int)

    '''
    IOP 5
    '''

    if iop is 5:

        if leg is 4:
            p_ind = np.where(np.logical_and(t >= 165053, t <= 165054))

        elif leg is 5:
            p_ind = np.where(np.logical_and(t >= 165749, t <= 165803))

        elif leg is 6:
            p_ind = np.where(np.logical_and(t >= 171814, t <= 171847))
            #p_ind = np.append(p_ind, np.where(np.logical_and(t >= 171728, t <= 171738)))
            #p_ind = np.where(np.logical_and(t >= 171728, t <= 171738))

        elif leg is 7:
            p_ind = np.where(np.logical_and(t >= 172839, t <= 172926))
            #p_ind = np.append(p_ind, np.where(np.logical_and(t >= 172951, t <= 173015)))
            #p_ind = np.where(np.logical_and(t >= 172951, t <= 173015))

        elif leg is 8:
            p_ind = np.where(np.logical_and(t >= 174121, t <= 174210))
            #p_ind = np.append(p_ind, np.where(np.logical_and(t >= 174050, t <= 174111)))
            #p_ind = np.where(np.logical_and(t >= 174050, t <= 174111))
        
        elif leg is 9:
            p_ind = np.where(np.logical_and(t >= 175850, t <= 175936))
            #p_ind = np.append(p_ind, np.where(np.logical_and(t >= 175951, t <= 180029)))
            #p_ind = np.where(np.logical_and(t >= 175951, t <= 180029))

        elif leg is 10:
            p_ind = np.where(np.logical_and(t >= 180410, t <= 180429))
            p_ind = np.append(p_ind, np.where(np.logical_and(t >= 180438, t <= 180458)))

        else:
            print ('**NO SEEDING PLUME**')

    return p_ind


def get_out_plume(
    ka,
    iop,
    leg,
    dist_out

    ):

    start, end = get_times(iop, leg=leg)[0], get_times(iop, leg=leg)[1]

    # filename = get_times(iop)+'.c1.nc'

    # if indir is not None:
    #     if indir[-1] is '/':
    #         ka = read_ka(indir+filename_ka)
    #     else:
    #         ka = read_ka(indir+'/'+filename_ka)
    # else:
    #     ka = read_ka(filename)

    t = np.array(ka.fields['HHMMSS']).astype(int)

    p_start = np.where(np.array(ka.fields['HHMMSS']) == str(start))[0][0]
    p_end = np.where(np.array(ka.fields['HHMMSS']) == str(end))[0][0]

    '''
    IOP 5
    '''

    if iop is 5:

        lats = ka.fields['lat']
        lons = ka.fields['lon']
        d = dist(lats, lons)[p_start:p_end]

        if leg is 4:
            end_plume_ind = np.where(t == 165053)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 5:
            end_plume_ind = np.where(t == 165803)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 6:
            end_plume_ind = np.where(t == 171728)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))
        
        if leg is 7:
            end_plume_ind = np.where(t == 173015)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))
        
        if leg is 8:
            end_plume_ind = np.where(t == 174050)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 9:
            end_plume_ind = np.where(t == 180029)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

        if leg is 10:
            end_plume_ind = np.where(t == 180438)[0][0]
            end_plume_d = dist(lats, lons)[end_plume_ind]
            d_ = d - end_plume_d
            out_plume = np.where(np.logical_and(d_ > 0, d_ <= dist_out))

    return out_plume


import numpy as np

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


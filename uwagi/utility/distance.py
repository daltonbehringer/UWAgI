import numpy as np

def dist(lats, lons):

	rlat, rlon = 44.207692, -116.0693

	ref_dist = 111.321 * np.cos(np.radians(lats))

	x_dist = (lons - rlon) * ref_dist
	y_dist = (lats - rlat) * 111.321

	dist = np.sqrt(x_dist**2 + y_dist**2)
	ind = np.where(dist[lons < rlon])
	dist[ind] = dist[ind] * -1

	return dist
'''
Start/end database for plotting function
'''


def which_data(
	iop = None,
	leg = None
	):

	# FINISH LATER (need to adjust plot function to accept IOP arg to select file.
	# IOP arg usage currently does not select file, only leg times)
	
	if iop is None or if leg is None:
		raise ValueError('Plotting function requires IOP and leg arguments.')
	
	elif iop is 1:
		date = '2017-01-08 '
		if leg is 1:
			start_time = date + '02:45:11'
			end_time = date + '02:56:09'
		elif leg is 2:
			start_time = date + '02:58:16'
			end_time = date + '03:16:13'
		elif leg is 3:
			start_time = date + '03:20:00'
			end_time = date + '03:27:35'
		elif leg is 4:
			start_time = date + '03:30:40'
			end_time = date + '03:50:57'
		elif leg is 5:
			start_time = date + '03:53:29'
			end_time = date + '04:05:07'
		elif leg is 6:
			start_time = date + '04:07:49'
			end_time = date + '04:29:09'
		elif leg is 7:
			start_time = date + '04:31:53'
			end_time = date + '04:43:00'
		elif leg is 8:
			start_time = date + '04:45:32'
			end_time = date + '05:06:52'
		elif leg is 9:
			start_time = date + '05:09:28'
			end_time = date + '05:21:04'
		elif leg is 10:
			start_time = date + '05:23:10'
			end_time = date + '05:31:30'

	elif iop is 2:
		date = '2017-01-09 '
		if leg is 1:
			start_time = date + '04:35:40'
			end_time = date + '04:46:00'
		elif leg is 2:
			start_time = date + '04:48:28'
			end_time = date + '05:06:08'
		elif leg is 3:
			start_time = date + '05:08:43'
			end_time = date + '05:17:26'
		elif leg is 4:
			start_time = date + '05:20:35'
			end_time = date + '05:38:03'
		elif leg is 5:
			start_time = date + '05:41:26'
			end_time = date + '05:50:30'
		elif leg is 6:
			start_time = date + '05:53:00'
			end_time = date + '06:13:58'
		elif leg is 7:
			start_time = date + '06:17:00'
			end_time = date + '06:28:10'
		elif leg is 8:
			start_time = date + '06:31:15'
			end_time = date + '06:50:11'
		elif leg is 9:
			start_time = date + '06:53:00'
			end_time = date + '07:04:52'
		elif leg is 10:
			start_time = date + '07:07:34'
			end_time = date + '07:26:40'

	elif iop is 3:
		date = '2017-01-11 '
		if leg is 1:
			start_time = date + '02:47:21'
			end_time = date + '03:03:35'
		elif leg is 2:
			start_time = date + '03:06:20'
			end_time = date + '03:24:18'
		elif leg is 3:
			start_time = date + '03:27:13'
			end_time = date + '03:34:17'
		elif leg is 4:
			start_time = date + '03:36:27'
			end_time = date + '03:51:40'
		elif leg is 5:
			start_time = date + '03:54:28'
			end_time = date + '04:02:56'
		elif leg is 6:
			start_time = date + '04:05:54'
			end_time = date + '04:23:06'
		elif leg is 7:
			start_time = date + '04:24:17'
			end_time = date + '04:35:32'
		elif leg is 8:
			start_time = date + '04:37:57'
			end_time = date + '04:58:24'
		elif leg is 9:
			start_time = date + '05:01:17'
			end_time = date + '05:13:08'
		elif leg is 10:
			start_time = date + '05:15:42'
			end_time = date + '05:28:09'



	return start_time, end_time


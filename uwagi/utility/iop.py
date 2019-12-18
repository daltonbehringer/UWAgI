'''
Function to define start/end time to flight legs
'''


def which_data(
	iop,
	leg
	):

	# FINISH LATER (need to adjust plot function to accept IOP arg to select file.
	# IOP arg usage currently does not select file, only leg times)
	
	if iop is None or leg is None:
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

	elif iop is 4:
		date = '2017-01-18 '
		if leg is 1:
			start_time = date + '20:15:40'
			end_time = date + '20:31:18'
		elif leg is 2:
			start_time = date + '20:33:42'
			end_time = date + '20:50:20'
		elif leg is 3:
			start_time = date + '20:52:56'
			end_time = date + '21:05:00'
		elif leg is 4:
			start_time = date + '21:07:28'
			end_time = date + '21:24:32'
		elif leg is 5:
			start_time = date + '21:27:10'
			end_time = date + '21:38:17'
		elif leg is 6:
			start_time = date + '21:40:50'
			end_time = date + '21:57:33'
		elif leg is 7:
			start_time = date + '22:00:09'
			end_time = date + '22:11:38'
		elif leg is 8:
			start_time = date + '22:13:06'
			end_time = date + '22:30:29'
		elif leg is 9:
			start_time = date + '22:33:00'
			end_time = date + '22:43:38'
		elif leg is 10:
			start_time = date + '22:46:16'
			end_time = date + '23:01:26'

	elif iop is 5:
		date = '2017-01-19 '
		if leg is 1:
			start_time = date + '15:40:02'
			end_time = date + '15:59:17'
		elif leg is 2:
			start_time = date + '16:02:13'
			end_time = date + '16:19:45'
		elif leg is 3:
			start_time = date + '16:22:31'
			end_time = date + '16:36:15'
		elif leg is 4:
			start_time = date + '16:39:47'
			end_time = date + '16:53:37'
		elif leg is 5:
			start_time = date + '16:55:51'
			end_time = date + '17:07:49'
		elif leg is 6:
			start_time = date + '17:10:13'
			end_time = date + '17:23:03'
		elif leg is 7:
			start_time = date + '17:25:20'
			end_time = date + '17:34:44'
		elif leg is 8:
			start_time = date + '17:37:58'
			end_time = date + '17:49:35'
		elif leg is 9:
			start_time = date + '17:51:57'
			end_time = date + '18:01:07'
		elif leg is 10:
			start_time = date + '18:03:40'
			end_time = date + '18:21:51'
	
	elif iop is 6:
		date1 = '2017-01-19 '
		date2 = '2017-01-20 '
		if leg is 1:
			start_time = date1 + '22:44:29'
			end_time = date1 + '23:05:05'
		elif leg is 2:
			start_time = date1 + '23:07:55'
			end_time = date1 + '23:25:12'
		elif leg is 3:
			start_time = date1 + '23:28:04'
			end_time = date1 + '23:43:10'
		elif leg is 4:
			start_time = date1 + '23:45:57'
			end_time = date2 + '00:02:27'
		elif leg is 5:
			start_time = date2 + '00:05:38'
			end_time = date2 + '00:19:38'
		elif leg is 6:
			start_time = date2 + '00:22:28'
			end_time = date2 + '00:39:08'
		elif leg is 7:
			start_time = date2 + '00:42:11'
			end_time = date2 + '00:57:13'
		elif leg is 8:
			start_time = date2 + '00:59:42'
			end_time = date2 + '01:16:30'
		elif leg is 9:
			start_time = date2 + '01:20:20'
			end_time = date2 + '01:36:01'
		elif leg is 10:
			start_time = date2 + '01:38:30'
			end_time = date2 + '01:52:00'

	elif iop is 7:
		date1 = '2017-01-21 '
		date2 = '2017-01-22 '
		if leg is 1:
			start_time = date1 + '22:49:40'
			end_time = date1 + '22:57:35'
		elif leg is 2:
			start_time = date1 + '23:00:00'
			end_time = date1 + '23:10:30'
		elif leg is 3:
			start_time = date1 + '23:13:00'
			end_time = date1 + '23:20:45'
		elif leg is 4:
			start_time = date1 + '23:25:30'
			end_time = date1 + '23:30:45'
		elif leg is 5:
			start_time = date1 + '23:33:25'
			end_time = date1 + '23:41:30'
		elif leg is 6:
			start_time = date1 + '23:44:00'
			end_time = date1 + '23:52:00'
		elif leg is 7:
			start_time = date1+ '23:55:00'
			end_time = date2 + '00:03:35'
		elif leg is 8:
			start_time = date2 + '00:06:30'
			end_time = date2 + '00:14:25'
		elif leg is 9:
			start_time = date2 + '00:17:20'
			end_time = date2 + '00:25:35'
		elif leg is 10:
			start_time = date2 + '00:28:15'
			end_time = date2 + '00:36:40'
		elif leg is 11:
			start_time = date2 + '00:39:50'
			end_time = date2 + '00:48:25'
		elif leg is 12:
			start_time = date2 + '00:51:20'
			end_time = date2 + '00:59:35'
		elif leg is 13:
			start_time = date2 + '01:02:30'
			end_time = date2 + '01:10:40'
		elif leg is 14:
			start_time = date2 + '01:15:50'
			end_time = date2 + '01:28:50'


	elif iop is 8:
		date1 = '2017-01-22 '
		date2 = '2017-01-23 '
		if leg is 1:
			start_time = date1 + '21:11:00'
			end_time = date1 + '21:23:05'
		elif leg is 2:
			start_time = date1 + '21:25:45'
			end_time = date1 + '21:41:00'
		elif leg is 3:
			start_time = date1 + '21:43:35'
			end_time = date1 + '21:50:45'
		elif leg is 4:
			start_time = date1 + '21:53:20'
			end_time = date1 + '22:05:35'
		elif leg is 5:
			start_time = date1 + '22:07:55'
			end_time = date1 + '22:18:10'
		elif leg is 6:
			start_time = date1 + '22:20:45'
			end_time = date1 + '22:38:20'
		elif leg is 7:
			start_time = date1+ '22:40:30'
			end_time = date1 + '22:52:20'
		elif leg is 8:
			start_time = date1 + '22:54:45'
			end_time = date1 + '23:12:38'
		elif leg is 9:
			start_time = date1 + '23:15:30'
			end_time = date1 + '23:26:30'
		elif leg is 10:
			start_time = date1 + '23:29:05'
			end_time = date1 + '23:46:15'
		elif leg is 11:
			start_time = date1 + '23:49:30'
			end_time = date2 + '00:00:30'
		elif leg is 12:
			start_time = date2 + '00:03:00'
			end_time = date2 + '00:20:20'

	elif iop is 9:
		date = '2017-01-31 '
		if leg is 1:
			start_time = date + '20:21:00'
			end_time = date + '20:31:00'
		elif leg is 2:
			start_time = date + '20:35:00'
			end_time = date + '20:52:15'
		elif leg is 3:
			start_time = date + '20:55:25'
			end_time = date + '20:58:05'
		elif leg is 4:
			start_time = date + '21:01:00'
			end_time = date + '21:06:10'
		elif leg is 5:
			start_time = date + '21:08:50'
			end_time = date + '21:12:45'
		elif leg is 6:
			start_time = date + '21:15:36'
			end_time = date + '21:19:48'
		elif leg is 7:
			start_time = date + '21:22:30'
			end_time = date + '21:28:30'
		elif leg is 8:
			start_time = date + '21:31:40'
			end_time = date + '21:38:40'
		elif leg is 9:
			start_time = date + '21:41:36'
			end_time = date + '21:44:48'
		elif leg is 10:
			start_time = date + '21:48:00'
			end_time = date + '22:01:00'

	elif iop is 10:
		date = '2017-02-03 '
		if leg is 1:
			start_time = date + '20:06:30'
			end_time = date + '20:17:55'
		elif leg is 2:
			start_time = date + '20:20:20'
			end_time = date + '20:37:54'
		elif leg is 3:
			start_time = date + '20:40:30'
			end_time = date + '20:50:10'
		elif leg is 4:
			start_time = date + '20:53:00'
			end_time = date + '21:03:40'
		elif leg is 5:
			start_time = date + '21:06:15'
			end_time = date + '21:13:25'
		elif leg is 6:
			start_time = date + '21:16:35'
			end_time = date + '21:24:50'


	return start_time, end_time


'''
Function to define start/end time to flight legs
'''

def get_times(
	iop,
	leg = None,
	start = None,
	end = None
	):

	# FINISH LATER (need to adjust plot function to accept IOP arg to select file.
	# IOP arg usage currently does not select file, only leg times)
	
	if iop is None:
		raise ValueError('Plotting function requires IOP argument.')
	
	elif iop is 1:
		date = '2017-01-08 '
		file = '20170108'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170109'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170111'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170118'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170119a'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170119b'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170121'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170122'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170131'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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
		file = '20170203'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
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

	elif iop is 11:
		date1 = '2017-02-04 '
		date2 = '2017-02-05 '
		file = '20170204'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date1 + '22:08:40'
			end_time = date1 + '22:18:00'
		elif leg is 2:
			start_time = date1 + '22:20:50'
			end_time = date1 + '22:38:50'
		elif leg is 3:
			start_time = date1 + '22:42:00'
			end_time = date1 + '22:52:30'
		elif leg is 4:
			start_time = date1 + '22:55:30'
			end_time = date1 + '23:11:30'
		elif leg is 5:
			start_time = date1 + '23:14:55'
			end_time = date1 + '23:27:00'
		elif leg is 6:
			start_time = date1 + '23:29:25'
			end_time = date1 + '23:43:05'
		elif leg is 7:
			start_time = date1+ '23:46:00'
			end_time = date1 + '23:56:35'
		elif leg is 8:
			start_time = date1 + '23:59:00'
			end_time = date2 + '00:12:20'
		elif leg is 9:
			start_time = date2 + '00:14:50'
			end_time = date2 + '00:25:40'
		elif leg is 10:
			start_time = date2 + '00:28:00'
			end_time = date2 + '00:42:30'
		elif leg is 11:
			start_time = date2 + '00:45:20'
			end_time = date2 + '00:56:05'
		elif leg is 12:
			start_time = date2 + '00:58:30'
			end_time = date2 + '01:07:10'

	elif iop is 12:
		date = '2017-02-07 '
		file = '20170207'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '20:13:30'
			end_time = date + '20:23:40'
		elif leg is 2:
			start_time = date + '20:26:15'
			end_time = date + '20:46:10'
		elif leg is 3:
			start_time = date + '20:49:35'
			end_time = date + '20:59:25'
		elif leg is 4:
			start_time = date + '21:02:30'
			end_time = date + '21:22:30'
		elif leg is 5:
			start_time = date + '21:25:10'
			end_time = date + '21:35:00'
		elif leg is 6:
			start_time = date + '21:37:00'
			end_time = date + '21:56:00'
		elif leg is 7:
			start_time = date + '21:59:30'
			end_time = date + '22:09:35'
		elif leg is 8:
			start_time = date + '22:12:34'
			end_time = date + '22:33:30'
		elif leg is 9:
			start_time = date + '22:36:30'
			end_time = date + '22:46:10'
		elif leg is 10:
			start_time = date + '22:49:00'
			end_time = date + '23:03:20'

	elif iop is 13:
		date1 = '2017-02-16 '
		date2 = '2017-02-17 '
		file = '20170216'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date1 + '23:42:54'
			end_time = date1 + '23:53:15'
		elif leg is 2:
			start_time = date1 + '23:58:00'
			end_time = date2 + '00:13:00'
		elif leg is 3:
			start_time = date2 + '00:15:50'
			end_time = date2 + '00:25:45'
		elif leg is 4:
			start_time = date2 + '00:29:00'
			end_time = date2 + '00:39:00'

	elif iop is 14:
		date1 = '2017-02-18 '
		date2 = '2017-02-19 '
		file = '20170218'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
				end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date1 + '21:45:00'
			end_time = date1 + '21:58:00'
		elif leg is 2:
			start_time = date1 + '22:01:00'
			end_time = date1 + '22:21:50'
		elif leg is 3:
			start_time = date1 + '22:23:40'
			end_time = date1 + '22:37:30'
		elif leg is 4:
			start_time = date1 + '22:39:20'
			end_time = date1 + '22:58:00'
		elif leg is 5:
			start_time = date1 + '23:00:40'
			end_time = date1 + '23:14:25'
		elif leg is 6:
			start_time = date1 + '23:16:20'
			end_time = date1 + '23:34:50'
		elif leg is 7:
			start_time = date1+ '23:36:25'
			end_time = date1 + '23:50:40'
		elif leg is 8:
			start_time = date1 + '23:52:00'
			end_time = date2 + '00:07:00'
		elif leg is 9:
			start_time = date2 + '00:10:30'
			end_time = date2 + '00:19:55'
		elif leg is 10:
			start_time = date2 + '00:21:50'
			end_time = date2 + '00:41:20'

	elif iop is 15:
		date = '2017-02-19 '
		file = '20170219'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '17:45:00'
			end_time = date + '17:55:09'
		elif leg is 2:
			start_time = date + '17:58:00'
			end_time = date + '18:15:00'
		elif leg is 3:
			start_time = date + '18:18:00'
			end_time = date + '18:30:45'
		elif leg is 4:
			start_time = date + '18:34:30'
			end_time = date + '18:46:20'
		elif leg is 5:
			start_time = date + '18:49:30'
			end_time = date + '18:58:35'
		elif leg is 6:
			start_time = date + '19:01:00'
			end_time = date + '19:10:00'
		elif leg is 7:
			start_time = date + '19:13:40'
			end_time = date + '19:19:00'
		elif leg is 8:
			start_time = date + '19:22:00'
			end_time = date + '19:39:00'
		elif leg is 9:
			start_time = date + '19:42:00'
			end_time = date + '19:57:30'
		elif leg is 10:
			start_time = date + '20:01:00'
			end_time = date + '20:14:30'
		elif leg is 11:
			start_time = date + '20:17:40'
			end_time = date + '20:27:00'
		elif leg is 12:
			start_time = date + '20:30:15'
			end_time = date + '20:45:30'

	elif iop is 16:
		date = '2017-02-20 '
		file = '20170220'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '14:47:15'
			end_time = date + '14:57:30'
		elif leg is 2:
			start_time = date + '15:01:00'
			end_time = date + '15:19:55'
		elif leg is 3:
			start_time = date + '15:24:35'
			end_time = date + '15:35:40'
		elif leg is 4:
			start_time = date + '15:38:45'
			end_time = date + '15:58:45'
		elif leg is 5:
			start_time = date + '16:01:45'
			end_time = date + '16:12:40'
		elif leg is 6:
			start_time = date + '16:15:15'
			end_time = date + '16:37:47'
		elif leg is 7:
			start_time = date + '16:40:40'
			end_time = date + '16:48:50'
		elif leg is 8:
			start_time = date + '17:03:02'
			end_time = date + '17:25:00'

	elif iop is 17:
		date = '2017-02-21 '
		file = '20170221'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '14:41:40'
			end_time = date + '14:52:40'
		elif leg is 2:
			start_time = date + '14:56:05'
			end_time = date + '15:15:50'
		elif leg is 3:
			start_time = date + '15:19:00'
			end_time = date + '15:30:54'
		elif leg is 4:
			start_time = date + '15:35:20'
			end_time = date + '15:53:40'
		elif leg is 5:
			start_time = date + '16:18:45'
			end_time = date + '16:31:15'
		elif leg is 6:
			start_time = date + '16:35:05'
			end_time = date + '16:52:30'
		elif leg is 7:
			start_time = date + '16:55:50'
			end_time = date + '17:06:20'
		elif leg is 8:
			start_time = date + '17:11:10'
			end_time = date + '17:25:30'
		elif leg is 9:
			start_time = date + '17:34:00'
			end_time = date + '17:44:15'
		elif leg is 10:
			start_time = date + '17:48:00'
			end_time = date + '18:06:40'

	elif iop is 19:
		date = '2017-03-04 '
		file = '20170304'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '13:30:00'
			end_time = date + '13:39:45'
		elif leg is 2:
			start_time = date + '13:43:30'
			end_time = date + '14:00:10'
		elif leg is 3:
			start_time = date + '14:03:40'
			end_time = date + '14:15:00'
		elif leg is 4:
			start_time = date + '14:18:45'
			end_time = date + '14:33:45'
		elif leg is 5:
			start_time = date + '14:36:30'
			end_time = date + '14:48:45'
		elif leg is 6:
			start_time = date + '14:51:20'
			end_time = date + '15:01:45'
		elif leg is 7:
			start_time = date + '15:04:25'
			end_time = date + '15:12:45'
		elif leg is 8:
			start_time = date + '15:14:15'
			end_time = date + '15:24:25'
		elif leg is 9:
			start_time = date + '15:27:30'
			end_time = date + '15:34:50'
		elif leg is 10:
			start_time = date + '15:37:50'
			end_time = date + '15:47:10'
		elif leg is 11:
			start_time = date + '15:50:20'
			end_time = date + '15:58:05'
		elif leg is 12:
			start_time = date + '16:00:05'
			end_time = date + '16:07:15'
		elif leg is 13:
			start_time = date + '16:10:05'
			end_time = date + '16:18:50'
		elif leg is 14:
			start_time = date + '16:25:40'
			end_time = date + '16:41:10'

	elif iop is 20:
		date = '2017-03-05 '
		file = '20170305'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '12:12:00'
			end_time = date + '12:22:30'
		elif leg is 2:
			start_time = date + '12:27:30'
			end_time = date + '12:44:20'
		elif leg is 3:
			start_time = date + '12:48:15'
			end_time = date + '12:59:35'
		elif leg is 4:
			start_time = date + '13:02:12'
			end_time = date + '13:17:00'
		elif leg is 5:
			start_time = date + '13:20:40'
			end_time = date + '13:29:30'
		elif leg is 6:
			start_time = date + '13:32:35'
			end_time = date + '13:47:00'
		elif leg is 7:
			start_time = date + '13:50:15'
			end_time = date + '13:59:00'
		elif leg is 8:
			start_time = date + '14:02:45'
			end_time = date + '14:17:05'
		elif leg is 9:
			start_time = date + '14:21:00'
			end_time = date + '14:30:15'
		elif leg is 10:
			start_time = date + '14:33:40'
			end_time = date + '14:52:00'

	elif iop is 21:
		date = '2017-03-07 '
		file = '20170307'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '14:23:40'
			end_time = date + '14:33:16'
		elif leg is 2:
			start_time = date + '14:36:20'
			end_time = date + '14:51:50'
		elif leg is 3:
			start_time = date + '14:55:20'
			end_time = date + '15:07:35'
		elif leg is 4:
			start_time = date + '15:09:18'
			end_time = date + '15:24:00'
		elif leg is 5:
			start_time = date + '15:26:50'
			end_time = date + '15:38:25'
		elif leg is 6:
			start_time = date + '15:40:30'
			end_time = date + '15:55:35'
		elif leg is 7:
			start_time = date + '15:58:20'
			end_time = date + '16:10:45'
		elif leg is 8:
			start_time = date + '16:13:05'
			end_time = date + '16:28:00'
		elif leg is 9:
			start_time = date + '16:31:00'
			end_time = date + '16:42:55'
		elif leg is 10:
			start_time = date + '16:45:09'
			end_time = date + '16:59:00'
		elif leg is 11:
			start_time = date + '17:01:40'
			end_time = date + '17:11:20'
		elif leg is 12:
			start_time = date + '17:12:55'
			end_time = date + '17:16:30'
		elif leg is 13:
			start_time = date + '17:18:25'
			end_time = date + '17:23:00'
		elif leg is 14:
			start_time = date + '17:25:23'
			end_time = date + '17:35:55'

	elif iop is 22:
		date = '2017-03-09 '
		file = '20170309a'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '14:22:15'
			end_time = date + '14:32:10'
		elif leg is 2:
			start_time = date + '14:35:05'
			end_time = date + '14:54:50'
		elif leg is 3:
			start_time = date + '14:58:22'
			end_time = date + '15:09:30'
		elif leg is 4:
			start_time = date + '15:13:00'
			end_time = date + '15:32:10'
		elif leg is 5:
			start_time = date + '15:36:00'
			end_time = date + '15:46:30'
		elif leg is 6:
			start_time = date + '15:50:40'
			end_time = date + '16:08:10'
		elif leg is 7:
			start_time = date + '16:11:40'
			end_time = date + '16:23:00'
		elif leg is 8:
			start_time = date + '16:26:30'
			end_time = date + '16:46:00'

	elif iop is 23:
		date = '2017-03-09 '
		file = '20170309b'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '20:19:45'
			end_time = date + '20:30:05'
		elif leg is 2:
			start_time = date + '20:34:00'
			end_time = date + '21:09:00'
		elif leg is 3:
			start_time = date + '21:13:00'
			end_time = date + '21:23:05'
		elif leg is 4:
			start_time = date + '21:27:30'
			end_time = date + '21:44:30'
		elif leg is 5:
			start_time = date + '21:48:00'
			end_time = date + '21:58:50'
		elif leg is 6:
			start_time = date + '22:02:40'
			end_time = date + '22:21:05'
		elif leg is 7:
			start_time = date + '22:24:30'
			end_time = date + '22:35:35'
		elif leg is 8:
			start_time = date + '22:40:00'
			end_time = date + '22:57:05'
		elif leg is 9:
			start_time = date + '23:00:10'
			end_time = date + '23:11:30'
		elif leg is 10:
			start_time = date + '23:15:35'
			end_time = date + '23:32:30'

	elif iop is 24:
		date = '2017-03-16 '
		file = '20170316a'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = date + '01:08:10'
			end_time = date + '01:18:20'
		elif leg is 2:
			start_time = date + '01:22:00'
			end_time = date + '01:40:40'
		elif leg is 3:
			start_time = date + '01:44:25'
			end_time = date + '01:54:30'
		elif leg is 4:
			start_time = date + '01:58:40'
			end_time = date + '02:15:25'
		elif leg is 5:
			start_time = date + '02:18:40'
			end_time = date + '02:30:20'
		elif leg is 6:
			start_time = date + '02:33:40'
			end_time = date + '02:51:20'
		elif leg is 7:
			start_time = date + '02:54:30'
			end_time = date + '03:06:15'
		elif leg is 8:
			start_time = date + '03:09:00'
			end_time = date + '03:27:00'
		elif leg is 9:
			start_time = date + '03:30:20'
			end_time = date + '03:41:40'
		elif leg is 10:
			start_time = date + '03:45:20'
			end_time = date + '04:02:25'
		elif leg is 11:
			start_time = date + '04:05:25'
			end_time = date + '04:09:30'
		elif leg is 12:
			start_time = date + '04:12:00'
			end_time = date + '04:20:30'

	if leg is None and start is None:
		return file
	else:
		return start_time, end_time, file


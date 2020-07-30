'''
Function to define start/end time to flight legs
'''

def get_times(
	iop,
	leg = None,
	start = None,
	end = None
	):
	
	if iop is None:
		raise ValueError('Function requires IOP argument.')
	
	elif iop is 1:
		date = '2017-01-08 '
		file = '20170108'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = '024511'
			end_time = '025609'
		elif leg is 2:
			start_time = '025816'
			end_time = '031613'
		elif leg is 3:
			start_time = '032000'
			end_time = '032735'
		elif leg is 4:
			start_time = '033040'
			end_time = '035057'
		elif leg is 5:
			start_time = '035329'
			end_time = '040507'
		elif leg is 6:
			start_time = '040749'
			end_time = '042909'
		elif leg is 7:
			start_time = '043153'
			end_time = '044300'
		elif leg is 8:
			start_time = '044532'
			end_time = '050652'
		elif leg is 9:
			start_time = '050928'
			end_time = '052104'
		elif leg is 10:
			start_time = '052310'
			end_time = '053130'

	elif iop is 2:
		date = '2017-01-09 '
		file = '20170109'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = '043540'
			end_time = '044600'
		elif leg is 2:
			start_time = '044828'
			end_time = '050608'
		elif leg is 3:
			start_time = '050843'
			end_time = '051726'
		elif leg is 4:
			start_time = '052035'
			end_time = '053803'
		elif leg is 5:
			start_time = '054126'
			end_time = '055030'
		elif leg is 6:
			start_time = '055300'
			end_time = '061358'
		elif leg is 7:
			start_time = '061700'
			end_time = '062810'
		elif leg is 8:
			start_time = '063115'
			end_time = '065011'
		elif leg is 9:
			start_time = '065300'
			end_time = '070452'
		elif leg is 10:
			start_time = '070734'
			end_time = '072640'

	elif iop is 3:
		date = '2017-01-11 '
		file = '20170111'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = '024721'
			end_time = '030335'
		elif leg is 2:
			start_time = '030620'
			end_time = '032418'
		elif leg is 3:
			start_time = '032713'
			end_time = '033417'
		elif leg is 4:
			start_time = '033627'
			end_time = '035140'
		elif leg is 5:
			start_time = '035428'
			end_time = '040256'
		elif leg is 6:
			start_time = '040554'
			end_time = '042306'
		elif leg is 7:
			start_time = '042417'
			end_time = '043532'
		elif leg is 8:
			start_time = '043757'
			end_time = '045824'
		elif leg is 9:
			start_time = '050117'
			end_time = '051308'
		elif leg is 10:
			start_time = '051542'
			end_time = '052809'

	elif iop is 4:
		date = '2017-01-18 '
		file = '20170118'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = '201540'
			end_time = '203118'
		elif leg is 2:
			start_time = '203342'
			end_time = '205020'
		elif leg is 3:
			start_time = '205256'
			end_time = '210500'
		elif leg is 4:
			start_time = '210728'
			end_time = '212432'
		elif leg is 5:
			start_time = '212710'
			end_time = '213817'
		elif leg is 6:
			start_time = '214050'
			end_time = '215733'
		elif leg is 7:
			start_time = '220009'
			end_time = '221138'
		elif leg is 8:
			start_time = '221306'
			end_time = '223029'
		elif leg is 9:
			start_time = '223300'
			end_time = '224338'
		elif leg is 10:
			start_time = '224616'
			end_time = '230126'

	elif iop is 5:
		date = '2017-01-19 '
		file = '20170119a'
		if leg is None and start is not None:
			start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
			end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
		elif leg is 1:
			start_time = '154002'
			end_time = '155917'
		elif leg is 2:
			start_time = '160213'
			end_time = '161945'
		elif leg is 3:
			start_time = '162231'
			end_time = '163615'
		elif leg is 4:
			start_time = '163947'
			end_time = '165337'
		elif leg is 5:
			start_time = '165551'
			end_time = '170749'
		elif leg is 6:
			start_time = '171013'
			end_time = '172303'
		elif leg is 7:
			start_time = '172520'
			end_time = '173444'
		elif leg is 8:
			start_time = '173758'
			end_time = '174935'
		elif leg is 9:
			start_time = '175157'
			end_time = '180107'
		elif leg is 10:
			start_time = '180340'
			end_time = '182151'
	
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
			start_time = '224429'
			end_time = '230505'
		elif leg is 2:
			start_time = '230755'
			end_time = '232512'
		elif leg is 3:
			start_time = '232804'
			end_time = '234310'
		elif leg is 4:
			start_time = '234557'
			end_time = '000227'
		elif leg is 5:
			start_time = '000538'
			end_time = '001938'
		elif leg is 6:
			start_time = '002228'
			end_time = '003908'
		elif leg is 7:
			start_time = '004211'
			end_time = '005713'
		elif leg is 8:
			start_time = '005942'
			end_time = '011630'
		elif leg is 9:
			start_time = '012020'
			end_time = '013601'
		elif leg is 10:
			start_time = '013830'
			end_time = '015200'

	# elif iop is 7:
	# 	date1 = '2017-01-21 '
	# 	date2 = '2017-01-22 '
	# 	file = '20170121'
	# 	if leg is None and start is not None:
	# 		if int(start[0:2]) > 20 and int(end[0:2]) > 20:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) <10 and int(end[0:2]) < 10:
	# 			start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 22:49:40
	# 		end_time = 22:57:35
	# 	elif leg is 2:
	# 		start_time = 23:00:00
	# 		end_time = 23:10:30
	# 	elif leg is 3:
	# 		start_time = 23:13:00
	# 		end_time = 23:20:45
	# 	elif leg is 4:
	# 		start_time = 23:25:30
	# 		end_time = 23:30:45
	# 	elif leg is 5:
	# 		start_time = 23:33:25
	# 		end_time = 23:41:30
	# 	elif leg is 6:
	# 		start_time = 23:44:00
	# 		end_time = 23:52:00
	# 	elif leg is 7:
	# 		start_time = 23:55:00
	# 		end_time = 03:35
	# 	elif leg is 8:
	# 		start_time = 06:30
	# 		end_time = 14:25
	# 	elif leg is 9:
	# 		start_time = 17:20
	# 		end_time = 25:35
	# 	elif leg is 10:
	# 		start_time = 28:15
	# 		end_time = 36:40
	# 	elif leg is 11:
	# 		start_time = 39:50
	# 		end_time = 48:25
	# 	elif leg is 12:
	# 		start_time = 51:20
	# 		end_time = 59:35
	# 	elif leg is 13:
	# 		start_time = 1:02:30
	# 		end_time = 1:10:40
	# 	elif leg is 14:
	# 		start_time = 1:15:50
	# 		end_time = 1:28:50


	# elif iop is 8:
	# 	date1 = '2017-01-22 '
	# 	date2 = '2017-01-23 '
	# 	file = '20170122'
	# 	if leg is None and start is not None:
	# 		if int(start[0:2]) > 20 and int(end[0:2]) > 20:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) <10 and int(end[0:2]) < 10:
	# 			start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 21:11:00
	# 		end_time = 21:23:05
	# 	elif leg is 2:
	# 		start_time = 21:25:45
	# 		end_time = 21:41:00
	# 	elif leg is 3:
	# 		start_time = 21:43:35
	# 		end_time = 21:50:45
	# 	elif leg is 4:
	# 		start_time = 21:53:20
	# 		end_time = 22:05:35
	# 	elif leg is 5:
	# 		start_time = 22:07:55
	# 		end_time = 22:18:10
	# 	elif leg is 6:
	# 		start_time = 22:20:45
	# 		end_time = 22:38:20
	# 	elif leg is 7:
	# 		start_time = 22:40:30
	# 		end_time = 22:52:20
	# 	elif leg is 8:
	# 		start_time = 22:54:45
	# 		end_time = 23:12:38
	# 	elif leg is 9:
	# 		start_time = 23:15:30
	# 		end_time = 23:26:30
	# 	elif leg is 10:
	# 		start_time = 23:29:05
	# 		end_time = 23:46:15
	# 	elif leg is 11:
	# 		start_time = 23:49:30
	# 		end_time = 00:30
	# 	elif leg is 12:
	# 		start_time = 03:00
	# 		end_time = 20:20

	# elif iop is 9:
	# 	date = '2017-01-31 '
	# 	file = '20170131'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 20:21:00
	# 		end_time = 20:31:00
	# 	elif leg is 2:
	# 		start_time = 20:35:00
	# 		end_time = 20:52:15
	# 	elif leg is 3:
	# 		start_time = 20:55:25
	# 		end_time = 20:58:05
	# 	elif leg is 4:
	# 		start_time = 21:01:00
	# 		end_time = 21:06:10
	# 	elif leg is 5:
	# 		start_time = 21:08:50
	# 		end_time = 21:12:45
	# 	elif leg is 6:
	# 		start_time = 21:15:36
	# 		end_time = 21:19:48
	# 	elif leg is 7:
	# 		start_time = 21:22:30
	# 		end_time = 21:28:30
	# 	elif leg is 8:
	# 		start_time = 21:31:40
	# 		end_time = 21:38:40
	# 	elif leg is 9:
	# 		start_time = 21:41:36
	# 		end_time = 21:44:48
	# 	elif leg is 10:
	# 		start_time = 21:48:00
	# 		end_time = 22:01:00

	# elif iop is 10:
	# 	date = '2017-02-03 '
	# 	file = '20170203'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 20:06:30
	# 		end_time = 20:17:55
	# 	elif leg is 2:
	# 		start_time = 20:20:20
	# 		end_time = 20:37:54
	# 	elif leg is 3:
	# 		start_time = 20:40:30
	# 		end_time = 20:50:10
	# 	elif leg is 4:
	# 		start_time = 20:53:00
	# 		end_time = 21:03:40
	# 	elif leg is 5:
	# 		start_time = 21:06:15
	# 		end_time = 21:13:25
	# 	elif leg is 6:
	# 		start_time = 21:16:35
	# 		end_time = 21:24:50

	# elif iop is 11:
	# 	date1 = '2017-02-04 '
	# 	date2 = '2017-02-05 '
	# 	file = '20170204'
	# 	if leg is None and start is not None:
	# 		if int(start[0:2]) > 20 and int(end[0:2]) > 20:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) <10 and int(end[0:2]) < 10:
	# 			start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 22:08:40
	# 		end_time = 22:18:00
	# 	elif leg is 2:
	# 		start_time = 22:20:50
	# 		end_time = 22:38:50
	# 	elif leg is 3:
	# 		start_time = 22:42:00
	# 		end_time = 22:52:30
	# 	elif leg is 4:
	# 		start_time = 22:55:30
	# 		end_time = 23:11:30
	# 	elif leg is 5:
	# 		start_time = 23:14:55
	# 		end_time = 23:27:00
	# 	elif leg is 6:
	# 		start_time = 23:29:25
	# 		end_time = 23:43:05
	# 	elif leg is 7:
	# 		start_time = 23:46:00
	# 		end_time = 23:56:35
	# 	elif leg is 8:
	# 		start_time = 23:59:00
	# 		end_time = 12:20
	# 	elif leg is 9:
	# 		start_time = 14:50
	# 		end_time = 25:40
	# 	elif leg is 10:
	# 		start_time = 28:00
	# 		end_time = 42:30
	# 	elif leg is 11:
	# 		start_time = 45:20
	# 		end_time = 56:05
	# 	elif leg is 12:
	# 		start_time = 58:30
	# 		end_time = 1:07:10

	# elif iop is 12:
	# 	date = '2017-02-07 '
	# 	file = '20170207'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 20:13:30
	# 		end_time = 20:23:40
	# 	elif leg is 2:
	# 		start_time = 20:26:15
	# 		end_time = 20:46:10
	# 	elif leg is 3:
	# 		start_time = 20:49:35
	# 		end_time = 20:59:25
	# 	elif leg is 4:
	# 		start_time = 21:02:30
	# 		end_time = 21:22:30
	# 	elif leg is 5:
	# 		start_time = 21:25:10
	# 		end_time = 21:35:00
	# 	elif leg is 6:
	# 		start_time = 21:37:00
	# 		end_time = 21:56:00
	# 	elif leg is 7:
	# 		start_time = 21:59:30
	# 		end_time = 22:09:35
	# 	elif leg is 8:
	# 		start_time = 22:12:34
	# 		end_time = 22:33:30
	# 	elif leg is 9:
	# 		start_time = 22:36:30
	# 		end_time = 22:46:10
	# 	elif leg is 10:
	# 		start_time = 22:49:00
	# 		end_time = 23:03:20

	# elif iop is 13:
	# 	date1 = '2017-02-16 '
	# 	date2 = '2017-02-17 '
	# 	file = '20170216'
	# 	if leg is None and start is not None:
	# 		if int(start[0:2]) > 20 and int(end[0:2]) > 20:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) <10 and int(end[0:2]) < 10:
	# 			start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 23:42:54
	# 		end_time = 23:53:15
	# 	elif leg is 2:
	# 		start_time = 23:58:00
	# 		end_time = 13:00
	# 	elif leg is 3:
	# 		start_time = 15:50
	# 		end_time = 25:45
	# 	elif leg is 4:
	# 		start_time = 29:00
	# 		end_time = 39:00

	# elif iop is 14:
	# 	date1 = '2017-02-18 '
	# 	date2 = '2017-02-19 '
	# 	file = '20170218'
	# 	if leg is None and start is not None:
	# 		if int(start[0:2]) > 20 and int(end[0:2]) > 20:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date1 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
	# 			start_time = date1 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 		elif int(start[0:2]) <10 and int(end[0:2]) < 10:
	# 			start_time = date2 + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 			end_time = date2 + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 21:45:00
	# 		end_time = 21:58:00
	# 	elif leg is 2:
	# 		start_time = 22:01:00
	# 		end_time = 22:21:50
	# 	elif leg is 3:
	# 		start_time = 22:23:40
	# 		end_time = 22:37:30
	# 	elif leg is 4:
	# 		start_time = 22:39:20
	# 		end_time = 22:58:00
	# 	elif leg is 5:
	# 		start_time = 23:00:40
	# 		end_time = 23:14:25
	# 	elif leg is 6:
	# 		start_time = 23:16:20
	# 		end_time = 23:34:50
	# 	elif leg is 7:
	# 		start_time = 23:36:25
	# 		end_time = 23:50:40
	# 	elif leg is 8:
	# 		start_time = 23:52:00
	# 		end_time = 07:00
	# 	elif leg is 9:
	# 		start_time = 10:30
	# 		end_time = 19:55
	# 	elif leg is 10:
	# 		start_time = 21:50
	# 		end_time = 41:20

	# elif iop is 15:
	# 	date = '2017-02-19 '
	# 	file = '20170219'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 17:45:00
	# 		end_time = 17:55:09
	# 	elif leg is 2:
	# 		start_time = 17:58:00
	# 		end_time = 18:15:00
	# 	elif leg is 3:
	# 		start_time = 18:18:00
	# 		end_time = 18:30:45
	# 	elif leg is 4:
	# 		start_time = 18:34:30
	# 		end_time = 18:46:20
	# 	elif leg is 5:
	# 		start_time = 18:49:30
	# 		end_time = 18:58:35
	# 	elif leg is 6:
	# 		start_time = 19:01:00
	# 		end_time = 19:10:00
	# 	elif leg is 7:
	# 		start_time = 19:13:40
	# 		end_time = 19:19:00
	# 	elif leg is 8:
	# 		start_time = 19:22:00
	# 		end_time = 19:39:00
	# 	elif leg is 9:
	# 		start_time = 19:42:00
	# 		end_time = 19:57:30
	# 	elif leg is 10:
	# 		start_time = 20:01:00
	# 		end_time = 20:14:30
	# 	elif leg is 11:
	# 		start_time = 20:17:40
	# 		end_time = 20:27:00
	# 	elif leg is 12:
	# 		start_time = 20:30:15
	# 		end_time = 20:45:30

	# elif iop is 16:
	# 	date = '2017-02-20 '
	# 	file = '20170220'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 14:47:15
	# 		end_time = 14:57:30
	# 	elif leg is 2:
	# 		start_time = 15:01:00
	# 		end_time = 15:19:55
	# 	elif leg is 3:
	# 		start_time = 15:24:35
	# 		end_time = 15:35:40
	# 	elif leg is 4:
	# 		start_time = 15:38:45
	# 		end_time = 15:58:45
	# 	elif leg is 5:
	# 		start_time = 16:01:45
	# 		end_time = 16:12:40
	# 	elif leg is 6:
	# 		start_time = 16:15:15
	# 		end_time = 16:37:47
	# 	elif leg is 7:
	# 		start_time = 16:40:40
	# 		end_time = 16:48:50
	# 	elif leg is 8:
	# 		start_time = 17:03:02
	# 		end_time = 17:25:00

	# elif iop is 17:
	# 	date = '2017-02-21 '
	# 	file = '20170221'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 14:41:40
	# 		end_time = 14:52:40
	# 	elif leg is 2:
	# 		start_time = 14:56:05
	# 		end_time = 15:15:50
	# 	elif leg is 3:
	# 		start_time = 15:19:00
	# 		end_time = 15:30:54
	# 	elif leg is 4:
	# 		start_time = 15:35:20
	# 		end_time = 15:53:40
	# 	elif leg is 5:
	# 		start_time = 16:18:45
	# 		end_time = 16:31:15
	# 	elif leg is 6:
	# 		start_time = 16:35:05
	# 		end_time = 16:52:30
	# 	elif leg is 7:
	# 		start_time = 16:55:50
	# 		end_time = 17:06:20
	# 	elif leg is 8:
	# 		start_time = 17:11:10
	# 		end_time = 17:25:30
	# 	elif leg is 9:
	# 		start_time = 17:34:00
	# 		end_time = 17:44:15
	# 	elif leg is 10:
	# 		start_time = 17:48:00
	# 		end_time = 18:06:40

	# elif iop is 19:
	# 	date = '2017-03-04 '
	# 	file = '20170304'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 13:30:00
	# 		end_time = 13:39:45
	# 	elif leg is 2:
	# 		start_time = 13:43:30
	# 		end_time = 14:00:10
	# 	elif leg is 3:
	# 		start_time = 14:03:40
	# 		end_time = 14:15:00
	# 	elif leg is 4:
	# 		start_time = 14:18:45
	# 		end_time = 14:33:45
	# 	elif leg is 5:
	# 		start_time = 14:36:30
	# 		end_time = 14:48:45
	# 	elif leg is 6:
	# 		start_time = 14:51:20
	# 		end_time = 15:01:45
	# 	elif leg is 7:
	# 		start_time = 15:04:25
	# 		end_time = 15:12:45
	# 	elif leg is 8:
	# 		start_time = 15:14:15
	# 		end_time = 15:24:25
	# 	elif leg is 9:
	# 		start_time = 15:27:30
	# 		end_time = 15:34:50
	# 	elif leg is 10:
	# 		start_time = 15:37:50
	# 		end_time = 15:47:10
	# 	elif leg is 11:
	# 		start_time = 15:50:20
	# 		end_time = 15:58:05
	# 	elif leg is 12:
	# 		start_time = 16:00:05
	# 		end_time = 16:07:15
	# 	elif leg is 13:
	# 		start_time = 16:10:05
	# 		end_time = 16:18:50
	# 	elif leg is 14:
	# 		start_time = 16:25:40
	# 		end_time = 16:41:10

	# elif iop is 20:
	# 	date = '2017-03-05 '
	# 	file = '20170305'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 12:12:00
	# 		end_time = 12:22:30
	# 	elif leg is 2:
	# 		start_time = 12:27:30
	# 		end_time = 12:44:20
	# 	elif leg is 3:
	# 		start_time = 12:48:15
	# 		end_time = 12:59:35
	# 	elif leg is 4:
	# 		start_time = 13:02:12
	# 		end_time = 13:17:00
	# 	elif leg is 5:
	# 		start_time = 13:20:40
	# 		end_time = 13:29:30
	# 	elif leg is 6:
	# 		start_time = 13:32:35
	# 		end_time = 13:47:00
	# 	elif leg is 7:
	# 		start_time = 13:50:15
	# 		end_time = 13:59:00
	# 	elif leg is 8:
	# 		start_time = 14:02:45
	# 		end_time = 14:17:05
	# 	elif leg is 9:
	# 		start_time = 14:21:00
	# 		end_time = 14:30:15
	# 	elif leg is 10:
	# 		start_time = 14:33:40
	# 		end_time = 14:52:00

	# elif iop is 21:
	# 	date = '2017-03-07 '
	# 	file = '20170307'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 14:23:40
	# 		end_time = 14:33:16
	# 	elif leg is 2:
	# 		start_time = 14:36:20
	# 		end_time = 14:51:50
	# 	elif leg is 3:
	# 		start_time = 14:55:20
	# 		end_time = 15:07:35
	# 	elif leg is 4:
	# 		start_time = 15:09:18
	# 		end_time = 15:24:00
	# 	elif leg is 5:
	# 		start_time = 15:26:50
	# 		end_time = 15:38:25
	# 	elif leg is 6:
	# 		start_time = 15:40:30
	# 		end_time = 15:55:35
	# 	elif leg is 7:
	# 		start_time = 15:58:20
	# 		end_time = 16:10:45
	# 	elif leg is 8:
	# 		start_time = 16:13:05
	# 		end_time = 16:28:00
	# 	elif leg is 9:
	# 		start_time = 16:31:00
	# 		end_time = 16:42:55
	# 	elif leg is 10:
	# 		start_time = 16:45:09
	# 		end_time = 16:59:00
	# 	elif leg is 11:
	# 		start_time = 17:01:40
	# 		end_time = 17:11:20
	# 	elif leg is 12:
	# 		start_time = 17:12:55
	# 		end_time = 17:16:30
	# 	elif leg is 13:
	# 		start_time = 17:18:25
	# 		end_time = 17:23:00
	# 	elif leg is 14:
	# 		start_time = 17:25:23
	# 		end_time = 17:35:55

	# elif iop is 22:
	# 	date = '2017-03-09 '
	# 	file = '20170309a'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 14:22:15
	# 		end_time = 14:32:10
	# 	elif leg is 2:
	# 		start_time = 14:35:05
	# 		end_time = 14:54:50
	# 	elif leg is 3:
	# 		start_time = 14:58:22
	# 		end_time = 15:09:30
	# 	elif leg is 4:
	# 		start_time = 15:13:00
	# 		end_time = 15:32:10
	# 	elif leg is 5:
	# 		start_time = 15:36:00
	# 		end_time = 15:46:30
	# 	elif leg is 6:
	# 		start_time = 15:50:40
	# 		end_time = 16:08:10
	# 	elif leg is 7:
	# 		start_time = 16:11:40
	# 		end_time = 16:23:00
	# 	elif leg is 8:
	# 		start_time = 16:26:30
	# 		end_time = 16:46:00

	# elif iop is 23:
	# 	date = '2017-03-09 '
	# 	file = '20170309b'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 20:19:45
	# 		end_time = 20:30:05
	# 	elif leg is 2:
	# 		start_time = 20:34:00
	# 		end_time = 21:09:00
	# 	elif leg is 3:
	# 		start_time = 21:13:00
	# 		end_time = 21:23:05
	# 	elif leg is 4:
	# 		start_time = 21:27:30
	# 		end_time = 21:44:30
	# 	elif leg is 5:
	# 		start_time = 21:48:00
	# 		end_time = 21:58:50
	# 	elif leg is 6:
	# 		start_time = 22:02:40
	# 		end_time = 22:21:05
	# 	elif leg is 7:
	# 		start_time = 22:24:30
	# 		end_time = 22:35:35
	# 	elif leg is 8:
	# 		start_time = 22:40:00
	# 		end_time = 22:57:05
	# 	elif leg is 9:
	# 		start_time = 23:00:10
	# 		end_time = 23:11:30
	# 	elif leg is 10:
	# 		start_time = 23:15:35
	# 		end_time = 23:32:30

	# elif iop is 24:
	# 	date = '2017-03-16 '
	# 	file = '20170316a'
	# 	if leg is None and start is not None:
	# 		start_time = date + start[0:2]+':'+start[2:4]+':'+start[4:6]
	# 		end_time = date + end[0:2]+':'+end[2:4]+':'+end[4:6]
	# 	elif leg is 1:
	# 		start_time = 1:08:10
	# 		end_time = 1:18:20
	# 	elif leg is 2:
	# 		start_time = 1:22:00
	# 		end_time = 1:40:40
	# 	elif leg is 3:
	# 		start_time = 1:44:25
	# 		end_time = 1:54:30
	# 	elif leg is 4:
	# 		start_time = 1:58:40
	# 		end_time = 2:15:25
	# 	elif leg is 5:
	# 		start_time = 2:18:40
	# 		end_time = 2:30:20
	# 	elif leg is 6:
	# 		start_time = 2:33:40
	# 		end_time = 2:51:20
	# 	elif leg is 7:
	# 		start_time = 2:54:30
	# 		end_time = 3:06:15
	# 	elif leg is 8:
	# 		start_time = 3:09:00
	# 		end_time = 3:27:00
	# 	elif leg is 9:
	# 		start_time = 3:30:20
	# 		end_time = 3:41:40
	# 	elif leg is 10:
	# 		start_time = 3:45:20
	# 		end_time = 4:02:25
	# 	elif leg is 11:
	# 		start_time = 4:05:25
	# 		end_time = 4:09:30
	# 	elif leg is 12:
	# 		start_time = 4:12:00
	# 		end_time = 4:20:30

	if leg is None and start is None:
		return file
	else:
		return start_time, end_time, file


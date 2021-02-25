'''
Function to define start/end time to flight legs and get proper file date/time

Returns: -file name if leg and start are 'None'
		 -[[start_time][end_time][file]] if leg or start/end included
'''

def get_times(
	iop = None,
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
			start_time = date + start[0:6]
			end_time = date + end[0:6]
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
			start_time = date + start[0:6]
			end_time = date + end[0:6]
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
			start_time = date + start[0:6]
			end_time = date + end[0:6]
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
			start_time = date + start[0:6]
			end_time = date + end[0:6]
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
			start_time = date + start[0:6]
			end_time = date + end[0:6]
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
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
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

	elif iop is 7:
		date1 = '2017-01-21 '
		date2 = '2017-01-22 '
		file = '20170121'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
		elif leg is 1:
			start_time = '224940'
			end_time = '225735'
		elif leg is 2:
			start_time = '230000'
			end_time = '231030'
		elif leg is 3:
			start_time = '231300'
			end_time = '232045'
		elif leg is 4:
			start_time = '232530'
			end_time = '233045'
		elif leg is 5:
			start_time = '233325'
			end_time = '234130'
		elif leg is 6:
			start_time = '234400'
			end_time = '235200'
		elif leg is 7:
			start_time = '235500'
			end_time = '000335'
		elif leg is 8:
			start_time = '000630'
			end_time = '001425'
		elif leg is 9:
			start_time = '001720'
			end_time = '002535'
		elif leg is 10:
			start_time = '002815'
			end_time = '003640'
		elif leg is 11:
			start_time = '003950'
			end_time = '004825'
		elif leg is 12:
			start_time = '005120'
			end_time = '005935'
		elif leg is 13:
			start_time = '010230'
			end_time = '011040'
		elif leg is 14:
			start_time = '011550'
			end_time = '012850'


	elif iop is 8:
		date1 = '2017-01-22 '
		date2 = '2017-01-23 '
		file = '20170122'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
		elif leg is 1:
			start_time = '211100'
			end_time = '212305'
		elif leg is 2:
			start_time = '212545'
			end_time = '214100'
		elif leg is 3:
			start_time = '214335'
			end_time = '215045'
		elif leg is 4:
			start_time = '215320'
			end_time = '220535'
		elif leg is 5:
			start_time = '220755'
			end_time = '221810'
		elif leg is 6:
			start_time = '222045'
			end_time = '223820'
		elif leg is 7:
			start_time = '224030'
			end_time = '225220'
		elif leg is 8:
			start_time = '225445'
			end_time = '231238'
		elif leg is 9:
			start_time = '231530'
			end_time = '232630'
		elif leg is 10:
			start_time = '232905'
			end_time = '234615'
		elif leg is 11:
			start_time = '234930'
			end_time = '000030'
		elif leg is 12:
			start_time = '000300'
			end_time = '002020'

	elif iop is 9:
		date = '2017-01-31 '
		file = '20170131'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '202100'
			end_time = '203100'
		elif leg is 2:
			start_time = '203500'
			end_time = '205215'
		elif leg is 3:
			start_time = '205525'
			end_time = '205805'
		elif leg is 4:
			start_time = '210100'
			end_time = '210610'
		elif leg is 5:
			start_time = '210850'
			end_time = '211245'
		elif leg is 6:
			start_time = '211536'
			end_time = '211948'
		elif leg is 7:
			start_time = '212230'
			end_time = '212830'
		elif leg is 8:
			start_time = '213140'
			end_time = '213840'
		elif leg is 9:
			start_time = '214136'
			end_time = '214448'
		elif leg is 10:
			start_time = '214800'
			end_time = '220100'

	elif iop is 10:
		date = '2017-02-03 '
		file = '20170203'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '200630'
			end_time = '201755'
		elif leg is 2:
			start_time = '202020'
			end_time = '203754'
		elif leg is 3:
			start_time = '204030'
			end_time = '205010'
		elif leg is 4:
			start_time = '205300'
			end_time = '210340'
		elif leg is 5:
			start_time = '210615'
			end_time = '211325'
		elif leg is 6:
			start_time = '211635'
			end_time = '212450'

	elif iop is 11:
		date1 = '2017-02-04 '
		date2 = '2017-02-05 '
		file = '20170204'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
		elif leg is 1:
			start_time = '220840'
			end_time = '221800'
		elif leg is 2:
			start_time = '222050'
			end_time = '223850'
		elif leg is 3:
			start_time = '224200'
			end_time = '225230'
		elif leg is 4:
			start_time = '225530'
			end_time = '231130'
		elif leg is 5:
			start_time = '231455'
			end_time = '232700'
		elif leg is 6:
			start_time = '232925'
			end_time = '234305'
		elif leg is 7:
			start_time = '234600'
			end_time = '235635'
		elif leg is 8:
			start_time = '235900'
			end_time = '001220'
		elif leg is 9:
			start_time = '001450'
			end_time = '002540'
		elif leg is 10:
			start_time = '002800'
			end_time = '004230'
		elif leg is 11:
			start_time = '004520'
			end_time = '005605'
		elif leg is 12:
			start_time = '005830'
			end_time = '010710'

	elif iop is 12:
		date = '2017-02-07 '
		file = '20170207'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '201330'
			end_time = '202340'
		elif leg is 2:
			start_time = '202615'
			end_time = '204610'
		elif leg is 3:
			start_time = '204935'
			end_time = '205925'
		elif leg is 4:
			start_time = '210230'
			end_time = '212230'
		elif leg is 5:
			start_time = '212510'
			end_time = '213500'
		elif leg is 6:
			start_time = '213700'
			end_time = '215600'
		elif leg is 7:
			start_time = '215930'
			end_time = '220935'
		elif leg is 8:
			start_time = '221234'
			end_time = '223330'
		elif leg is 9:
			start_time = '223630'
			end_time = '224610'
		elif leg is 10:
			start_time = '224900'
			end_time = '230320'

	elif iop is 13:
		date1 = '2017-02-16 '
		date2 = '2017-02-17 '
		file = '20170216'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
		elif leg is 1:
			start_time = '234254'
			end_time = '235315'
		elif leg is 2:
			start_time = '235800'
			end_time = '001300'
		elif leg is 3:
			start_time = '001550'
			end_time = '002545'
		elif leg is 4:
			start_time = '002900'
			end_time = '003900'

	elif iop is 14:
		date1 = '2017-02-18 '
		date2 = '2017-02-19 '
		file = '20170218'
		if leg is None and start is not None:
			if int(start[0:2]) > 20 and int(end[0:2]) > 20:
				start_time = date1 + start[0:6]
				end_time = date1 + end[0:6]
			elif int(start[0:2]) > 20 and int(end[0:2]) < 10:
				start_time = date1 + start[0:6]
				end_time = date2 + end[0:6]
			elif int(start[0:2]) <10 and int(end[0:2]) < 10:
				start_time = date2 + start[0:6]
				end_time = date2 + end[0:6]
		elif leg is 1:
			start_time = '214500'
			end_time = '215800'
		elif leg is 2:
			start_time = '220100'
			end_time = '222150'
		elif leg is 3:
			start_time = '222340'
			end_time = '223730'
		elif leg is 4:
			start_time = '223920'
			end_time = '225800'
		elif leg is 5:
			start_time = '230040'
			end_time = '231425'
		elif leg is 6:
			start_time = '231620'
			end_time = '233450'
		elif leg is 7:
			start_time = '233625'
			end_time = '235040'
		elif leg is 8:
			start_time = '235200'
			end_time = '000700'
		elif leg is 9:
			start_time = '001030'
			end_time = '001955'
		elif leg is 10:
			start_time = '002150'
			end_time = '004120'

	elif iop is 15:
		date = '2017-02-19 '
		file = '20170219'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '174500'
			end_time = '175509'
		elif leg is 2:
			start_time = '175800'
			end_time = '181500'
		elif leg is 3:
			start_time = '181800'
			end_time = '183045'
		elif leg is 4:
			start_time = '183430'
			end_time = '184620'
		elif leg is 5:
			start_time = '184930'
			end_time = '185835'
		elif leg is 6:
			start_time = '190100'
			end_time = '191000'
		elif leg is 7:
			start_time = '191340'
			end_time = '191900'
		elif leg is 8:
			start_time = '192200'
			end_time = '193900'
		elif leg is 9:
			start_time = '194200'
			end_time = '195730'
		elif leg is 10:
			start_time = '200100'
			end_time = '201430'
		elif leg is 11:
			start_time = '201740'
			end_time = '202700'
		elif leg is 12:
			start_time = '203015'
			end_time = '204530'

	elif iop is 16:
		date = '2017-02-20 '
		file = '20170220'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '144715'
			end_time = '145730'
		elif leg is 2:
			start_time = '150100'
			end_time = '151955'
		elif leg is 3:
			start_time = '152435'
			end_time = '153540'
		elif leg is 4:
			start_time = '153845'
			end_time = '155845'
		elif leg is 5:
			start_time = '160145'
			end_time = '161240'
		elif leg is 6:
			start_time = '161515'
			end_time = '163747'
		elif leg is 7:
			start_time = '164040'
			end_time = '164850'
		elif leg is 8:
			start_time = '170302'
			end_time = '172500'

	elif iop is 17:
		date = '2017-02-21 '
		file = '20170221'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '144140'
			end_time = '145240'
		elif leg is 2:
			start_time = '145605'
			end_time = '151550'
		elif leg is 3:
			start_time = '151900'
			end_time = '153054'
		elif leg is 4:
			start_time = '153520'
			end_time = '155340'
		elif leg is 5:
			start_time = '161845'
			end_time = '163115'
		elif leg is 6:
			start_time = '163505'
			end_time = '165230'
		elif leg is 7:
			start_time = '165550'
			end_time = '170620'
		elif leg is 8:
			start_time = '171110'
			end_time = '172530'
		elif leg is 9:
			start_time = '173400'
			end_time = '174415'
		elif leg is 10:
			start_time = '174800'
			end_time = '180640'

	elif iop is 19:
		date = '2017-03-04 '
		file = '20170304'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '133000'
			end_time = '133945'
		elif leg is 2:
			start_time = '134330'
			end_time = '140010'
		elif leg is 3:
			start_time = '140340'
			end_time = '141500'
		elif leg is 4:
			start_time = '141845'
			end_time = '143345'
		elif leg is 5:
			start_time = '143630'
			end_time = '144845'
		elif leg is 6:
			start_time = '145120'
			end_time = '150145'
		elif leg is 7:
			start_time = '150425'
			end_time = '151245'
		elif leg is 8:
			start_time = '151415'
			end_time = '152425'
		elif leg is 9:
			start_time = '152730'
			end_time = '153450'
		elif leg is 10:
			start_time = '153750'
			end_time = '154710'
		elif leg is 11:
			start_time = '155020'
			end_time = '155805'
		elif leg is 12:
			start_time = '160005'
			end_time = '160715'
		elif leg is 13:
			start_time = '161005'
			end_time = '161850'
		elif leg is 14:
			start_time = '162540'
			end_time = '164110'

	elif iop is 20:
		date = '2017-03-05 '
		file = '20170305'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '121200'
			end_time = '122230'
		elif leg is 2:
			start_time = '122730'
			end_time = '124420'
		elif leg is 3:
			start_time = '124815'
			end_time = '125935'
		elif leg is 4:
			start_time = '130212'
			end_time = '131700'
		elif leg is 5:
			start_time = '132040'
			end_time = '132930'
		elif leg is 6:
			start_time = '133235'
			end_time = '134700'
		elif leg is 7:
			start_time = '135015'
			end_time = '135900'
		elif leg is 8:
			start_time = '140245'
			end_time = '141705'
		elif leg is 9:
			start_time = '142100'
			end_time = '143015'
		elif leg is 10:
			start_time = '143340'
			end_time = '145200'

	elif iop is 21:
		date = '2017-03-07 '
		file = '20170307'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '142340'
			end_time = '143316'
		elif leg is 2:
			start_time = '143620'
			end_time = '145150'
		elif leg is 3:
			start_time = '145520'
			end_time = '150735'
		elif leg is 4:
			start_time = '150918'
			end_time = '152400'
		elif leg is 5:
			start_time = '152650'
			end_time = '153825'
		elif leg is 6:
			start_time = '154030'
			end_time = '155535'
		elif leg is 7:
			start_time = '155820'
			end_time = '161045'
		elif leg is 8:
			start_time = '161305'
			end_time = '162800'
		elif leg is 9:
			start_time = '163100'
			end_time = '164255'
		elif leg is 10:
			start_time = '164509'
			end_time = '165900'
		elif leg is 11:
			start_time = '170140'
			end_time = '171120'
		elif leg is 12:
			start_time = '171255'
			end_time = '171630'
		elif leg is 13:
			start_time = '171825'
			end_time = '172300'
		elif leg is 14:
			start_time = '172523'
			end_time = '173555'

	elif iop is 22:
		date = '2017-03-09 '
		file = '20170309a'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '142215'
			end_time = '143210'
		elif leg is 2:
			start_time = '143505'
			end_time = '145450'
		elif leg is 3:
			start_time = '145822'
			end_time = '150930'
		elif leg is 4:
			start_time = '151300'
			end_time = '153210'
		elif leg is 5:
			start_time = '153600'
			end_time = '154630'
		elif leg is 6:
			start_time = '155040'
			end_time = '160810'
		elif leg is 7:
			start_time = '161140'
			end_time = '162300'
		elif leg is 8:
			start_time = '162630'
			end_time = '164600'

	elif iop is 23:
		date = '2017-03-09 '
		file = '20170309b'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '201945'
			end_time = '203005'
		elif leg is 2:
			start_time = '203400'
			end_time = '210900'
		elif leg is 3:
			start_time = '211300'
			end_time = '212305'
		elif leg is 4:
			start_time = '212730'
			end_time = '214430'
		elif leg is 5:
			start_time = '214800'
			end_time = '215850'
		elif leg is 6:
			start_time = '220240'
			end_time = '222105'
		elif leg is 7:
			start_time = '222430'
			end_time = '223535'
		elif leg is 8:
			start_time = '224000'
			end_time = '225705'
		elif leg is 9:
			start_time = '230010'
			end_time = '231130'
		elif leg is 10:
			start_time = '231535'
			end_time = '233230'

	elif iop is 24:
		date = '2017-03-16 '
		file = '20170316a'
		if leg is None and start is not None:
			start_time = date + start[0:6]
			end_time = date + end[0:6]
		elif leg is 1:
			start_time = '010810'
			end_time = '011820'
		elif leg is 2:
			start_time = '012200'
			end_time = '014040'
		elif leg is 3:
			start_time = '014425'
			end_time = '015430'
		elif leg is 4:
			start_time = '015840'
			end_time = '021525'
		elif leg is 5:
			start_time = '021840'
			end_time = '023020'
		elif leg is 6:
			start_time = '023340'
			end_time = '025120'
		elif leg is 7:
			start_time = '025430'
			end_time = '030615'
		elif leg is 8:
			start_time = '030900'
			end_time = '032700'
		elif leg is 9:
			start_time = '033020'
			end_time = '034140'
		elif leg is 10:
			start_time = '034520'
			end_time = '040225'
		elif leg is 11:
			start_time = '040525'
			end_time = '040930'
		elif leg is 12:
			start_time = '041200'
			end_time = '042030'

	if leg is None and start is None:
		return file
	else:
		return start_time, end_time, file


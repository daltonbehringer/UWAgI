'''
Labels function for variables
'''

def get_label(var):

	if var is 'lat':
		label = 'Latitude'
	if var is 'lon':
		label = 'Longitude'
	if var is 'temperature':
		label = r'Temperature, $^\circ$C'
	if var is 'dewpoint':
		label = r'Dewpoint Temp., $^\circ$C'
	if var is 'wind_mag':
		label = r'Wind Speed, $m\/s^{-1}$'
	if var is 'wind_dir':
		label = r'Wind Direction, $deg$'
	if var is 'lwc100':
		label = r'Liquid Water Content, $g\/m^{-3}$'
	if var is 'nev_lwc':
		label = r'Nevzorov Liquid Water Content, $g\/m^{-3}$'
	if var is 'nev_twc':
		label = r'Nevzorov Total Water Content, $g\/m^{-3}$'
	if var is 'nev_iwc':
		label = r'Nevzorov Ice Water Content, $g\/m^{-3}$'
	if var is 'cdp_lwc':
		label = r'CDP Liquid Water Content, $g\/m^{-3}$'
	# if var is 'cdp_conc':
	# 	label = 'CDP Total Concentraion, $cm^{-3}$'
	if var is 'cdp_conc':
		label = r'CDP Total Concentraion, $cm^{-3}$'
	if var is 'lwc_pvm':
		label = r'PVM Liquid Water Content, $g\/m^{-3}$'


	return label
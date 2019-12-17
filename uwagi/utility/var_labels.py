'''
Labels function for variables
'''

def get_label(var):

	if var is 'temperature':
		label = 'Temperature, $^\circ$C'
	if var is 'dewpoint':
		label = 'Dewpoint Temp., $^\circ$C'
	if var is 'wind_mag':
		label = 'Wind Speed, ms$^{-1}$'
	if var is 'wind_dir':
		label = 'Wind Direction, deg'
	if var is 'lwc100':
		label = 'Liquid Water Content, gm$^{-3}$'
	if var is 'nev_lwc':
		label = 'Nevzorov Liquid Water Content, gm$^{-3}$'
	if var is 'nev_twc':
		label = 'Nevzorov Total Water Content, gm$^{-3}$'
	if var is 'cdp_lwc':
		label = 'CDP Liquid Water Content, gm$^{-3}$'
	if var is 'cdp_conc':
		label = 'CDP Total Concentraion, cm$^{-3}$'
	if var is 'lwc_pvm':
		label = 'PVM Liquid Water Content, gm$^{-3}$'

	return label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

font = {'family': 'sans serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
labelsize = 12

outdir = '/Users/jbehrin1/Desktop/snowie_data/'

'''
Requires plume stats csv from get_plume_stats.csv

This is currently not automated. You will need to write code to automate, 
or manually create csv from get_plume_stats.py output (as of 06/04/21).
'''
df = pd.read_csv('~/Desktop/snowie_data/csv/plumestats_IOP5.csv')

segment  = 'in'
out_dist = 2.7 ### km

if segment is 'out':
	df_ = df[df.Segment == segment+'_'+str(out_dist)[0]+'_'+str(out_dist)[2]]
else:
	df_ = df[df.Segment == segment]

var = 'Ice'

df_ = df_.reset_index(drop=True)

if segment is 'full':

	boxes = [
		{
			'label' : df_['Leg'][0],
			'whislo': df_[var+'10'][0],
			'q1'    : df_[var+'25'][0],
			'med'   : df_[var+'Mean'][0],
			'q3'    : df_[var+'75'][0],
			'whishi': df_[var+'90'][0],
			'fliers': []
		},
		{
			'label' : df_['Leg'][1],
			'whislo': df_[var+'10'][1],
			'q1'    : df_[var+'25'][1],
			'med'   : df_[var+'Mean'][1],
			'q3'    : df_[var+'75'][1],
			'whishi': df_[var+'90'][1],
			'fliers': []
		},
		{
			'label' : df_['Leg'][2],
			'whislo': df_[var+'10'][2],
			'q1'    : df_[var+'25'][2],
			'med'   : df_[var+'Mean'][2],
			'q3'    : df_[var+'75'][2],
			'whishi': df_[var+'90'][2],
			'fliers': []
		},
		{
			'label' : df_['Leg'][3],
			'whislo': df_[var+'10'][3],
			'q1'    : df_[var+'25'][3],
			'med'   : df_[var+'Mean'][3],
			'q3'    : df_[var+'75'][3],
			'whishi': df_[var+'90'][3],
			'fliers': []
		},
		{
			'label' : df_['Leg'][4],
			'whislo': df_[var+'10'][4],
			'q1'    : df_[var+'25'][4],
			'med'   : df_[var+'Mean'][4],
			'q3'    : df_[var+'75'][4],
			'whishi': df_[var+'90'][4],
			'fliers': []
		},
		{
			'label' : df_['Leg'][5],
			'whislo': df_[var+'10'][5],
			'q1'    : df_[var+'25'][5],
			'med'   : df_[var+'Mean'][5],
			'q3'    : df_[var+'75'][5],
			'whishi': df_[var+'90'][5],
			'fliers': []
		},
		{
			'label' : df_['Leg'][6],
			'whislo': df_[var+'10'][6],
			'q1'    : df_[var+'25'][6],
			'med'   : df_[var+'Mean'][6],
			'q3'    : df_[var+'75'][6],
			'whishi': df_[var+'90'][6],
			'fliers': []
		},
		{
			'label' : df_['Leg'][7],
			'whislo': df_[var+'10'][7],
			'q1'    : df_[var+'25'][7],
			'med'   : df_[var+'Mean'][7],
			'q3'    : df_[var+'75'][7],
			'whishi': df_[var+'90'][7],
			'fliers': []
		},
		{
			'label' : df_['Leg'][8],
			'whislo': df_[var+'10'][8],
			'q1'    : df_[var+'25'][8],
			'med'   : df_[var+'Mean'][8],
			'q3'    : df_[var+'75'][8],
			'whishi': df_[var+'90'][8],
			'fliers': []
		},
		{
			'label' : df_['Leg'][9],
			'whislo': df_[var+'10'][9],
			'q1'    : df_[var+'25'][9],
			'med'   : df_[var+'Mean'][9],
			'q3'    : df_[var+'75'][9],
			'whishi': df_[var+'90'][9],
			'fliers': []
		}
	]
	
if segment is 'out':

	boxes = [
		{
			'label' : df_['Leg'][0],
			'whislo': df_[var+'10'][0],
			'q1'    : df_[var+'25'][0],
			'med'   : df_[var+'Mean'][0],
			'q3'    : df_[var+'75'][0],
			'whishi': df_[var+'90'][0],
			'fliers': []
		},
		{
			'label' : df_['Leg'][1],
			'whislo': df_[var+'10'][1],
			'q1'    : df_[var+'25'][1],
			'med'   : df_[var+'Mean'][1],
			'q3'    : df_[var+'75'][1],
			'whishi': df_[var+'90'][1],
			'fliers': []
		},
		{
			'label' : df_['Leg'][2],
			'whislo': df_[var+'10'][2],
			'q1'    : df_[var+'25'][2],
			'med'   : df_[var+'Mean'][2],
			'q3'    : df_[var+'75'][2],
			'whishi': df_[var+'90'][2],
			'fliers': []
		},
		{
			'label' : df_['Leg'][3],
			'whislo': df_[var+'10'][3],
			'q1'    : df_[var+'25'][3],
			'med'   : df_[var+'Mean'][3],
			'q3'    : df_[var+'75'][3],
			'whishi': df_[var+'90'][3],
			'fliers': []
		},
		{
			'label' : df_['Leg'][4],
			'whislo': df_[var+'10'][4],
			'q1'    : df_[var+'25'][4],
			'med'   : df_[var+'Mean'][4],
			'q3'    : df_[var+'75'][4],
			'whishi': df_[var+'90'][4],
			'fliers': []
		},
		{
			'label' : df_['Leg'][5],
			'whislo': df_[var+'10'][5],
			'q1'    : df_[var+'25'][5],
			'med'   : df_[var+'Mean'][5],
			'q3'    : df_[var+'75'][5],
			'whishi': df_[var+'90'][5],
			'fliers': []
		},
		{
			'label' : df_['Leg'][6],
			'whislo': df_[var+'10'][6],
			'q1'    : df_[var+'25'][6],
			'med'   : df_[var+'Mean'][6],
			'q3'    : df_[var+'75'][6],
			'whishi': df_[var+'90'][6],
			'fliers': []
		}
	]

if segment is 'in':

	boxes = [
		{
			'label' : df_['Leg'][0],
			'whislo': df_[var+'10'][0],
			'q1'    : df_[var+'25'][0],
			'med'   : df_[var+'Mean'][0],
			'q3'    : df_[var+'75'][0],
			'whishi': df_[var+'90'][0],
			'fliers': []
		},
		{
			'label' : df_['Leg'][1],
			'whislo': df_[var+'10'][1],
			'q1'    : df_[var+'25'][1],
			'med'   : df_[var+'Mean'][1],
			'q3'    : df_[var+'75'][1],
			'whishi': df_[var+'90'][1],
			'fliers': []
		},
		{
			'label' : df_['Leg'][2],
			'whislo': df_[var+'10'][2],
			'q1'    : df_[var+'25'][2],
			'med'   : df_[var+'Mean'][2],
			'q3'    : df_[var+'75'][2],
			'whishi': df_[var+'90'][2],
			'fliers': []
		},
		{
			'label' : df_['Leg'][3],
			'whislo': df_[var+'10'][3],
			'q1'    : df_[var+'25'][3],
			'med'   : df_[var+'Mean'][3],
			'q3'    : df_[var+'75'][3],
			'whishi': df_[var+'90'][3],
			'fliers': []
		},
		{
			'label' : df_['Leg'][4],
			'whislo': df_[var+'10'][4],
			'q1'    : df_[var+'25'][4],
			'med'   : df_[var+'Mean'][4],
			'q3'    : df_[var+'75'][4],
			'whishi': df_[var+'90'][4],
			'fliers': []
		},
		{
			'label' : df_['Leg'][5],
			'whislo': df_[var+'10'][5],
			'q1'    : df_[var+'25'][5],
			'med'   : df_[var+'Mean'][5],
			'q3'    : df_[var+'75'][5],
			'whishi': df_[var+'90'][5],
			'fliers': []
		},
		{
			'label' : df_['Leg'][6],
			'whislo': df_[var+'10'][6],
			'q1'    : df_[var+'25'][6],
			'med'   : df_[var+'Mean'][6],
			'q3'    : df_[var+'75'][6],
			'whishi': df_[var+'90'][6],
			'fliers': []
		},
		{
			'label' : df_['Leg'][7],
			'whislo': df_[var+'10'][7],
			'q1'    : df_[var+'25'][7],
			'med'   : df_[var+'Mean'][7],
			'q3'    : df_[var+'75'][7],
			'whishi': df_[var+'90'][7],
			'fliers': []
		},
		{
			'label' : df_['Leg'][8],
			'whislo': df_[var+'10'][8],
			'q1'    : df_[var+'25'][8],
			'med'   : df_[var+'Mean'][8],
			'q3'    : df_[var+'75'][8],
			'whishi': df_[var+'90'][8],
			'fliers': []
		},
		{
			'label' : df_['Leg'][9],
			'whislo': df_[var+'10'][9],
			'q1'    : df_[var+'25'][9],
			'med'   : df_[var+'Mean'][9],
			'q3'    : df_[var+'75'][9],
			'whishi': df_[var+'90'][9],
			'fliers': []
		},
		{
			'label' : df_['Leg'][10],
			'whislo': df_[var+'10'][10],
			'q1'    : df_[var+'25'][10],
			'med'   : df_[var+'Mean'][10],
			'q3'    : df_[var+'75'][10],
			'whishi': df_[var+'90'][10],
			'fliers': []
		},
		{
			'label' : df_['Leg'][11],
			'whislo': df_[var+'10'][11],
			'q1'    : df_[var+'25'][11],
			'med'   : df_[var+'Mean'][11],
			'q3'    : df_[var+'75'][11],
			'whishi': df_[var+'90'][11],
			'fliers': []
		},
		{
			'label' : df_['Leg'][12],
			'whislo': df_[var+'10'][12],
			'q1'    : df_[var+'25'][12],
			'med'   : df_[var+'Mean'][12],
			'q3'    : df_[var+'75'][12],
			'whishi': df_[var+'90'][12],
			'fliers': []
		},
		{
			'label' : df_['Leg'][13],
			'whislo': df_[var+'10'][13],
			'q1'    : df_[var+'25'][13],
			'med'   : df_[var+'Mean'][13],
			'q3'    : df_[var+'75'][13],
			'whishi': df_[var+'90'][13],
			'fliers': []
		},
		{
			'label' : df_['Leg'][14],
			'whislo': df_[var+'10'][14],
			'q1'    : df_[var+'25'][14],
			'med'   : df_[var+'Mean'][14],
			'q3'    : df_[var+'75'][14],
			'whishi': df_[var+'90'][14],
			'fliers': []
		}
	]

fig = plt.figure(figsize=(7,6))
ax = plt.gca()

ax.bxp(boxes, showfliers=False)
ax.set_ylim([0,0.25])
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.02))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))

if var is 'CDP':
	ax.set_ylabel(r'CDP LWC (g$\/$m$^{-3})$', fontdict=font)
if var is 'Nev':
	ax.set_ylabel(r'Nevzorov LWC (g$\/$m$^{-3})$', fontdict=font)
if var is 'Ice':
	ax.set_ylabel(r'Nevzorov IWC (g$\/$m$^{-3})$', fontdict=font)

if segment is 'in':
	ax.set_title('IOP 5 Water Content (In-plume)', fontdict=font)
if segment is 'out':
	ax.set_title('IOP 5 Water Content (Out-of-plume) | ' +
		'Downwind Dist = ' + str(out_dist) + ' km', fontdict=font)
if segment is 'full':
	ax.set_title('IOP 5 Water Content (Full leg)', fontdict=font)

ax.set_xlabel('Leg', fontdict=font)

ax.tick_params(axis='both', which='major', direction='in', grid_linestyle='--', grid_alpha=0.5,
    length=7, labelsize=labelsize)
ax.tick_params(axis='y', which='minor', direction='in',length=4, labelsize=labelsize)
ax.grid(True, axis='y', ls=':', alpha=0.75)

if segment is 'in' or segment is 'full':
	plt.savefig(outdir + 'plumestats_IOP5_' +
		var + '_' + segment, 
		dpi=300, bbox_inches = 'tight', pad_inches = 0.1)

if segment is 'out':
	plt.savefig(outdir + 'plumestats_IOP5_' +
		var + '_' + segment + str(out_dist)[0] + str(out_dist)[2], 
		dpi=300, bbox_inches = 'tight', pad_inches = 0.1)

plt.show()


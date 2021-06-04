import uwagi
import matplotlib.pyplot as plt
import sys

func = int(sys.argv[1])

indir = '/Volumes/Daltons_Archive/snowie_data/allKA'
outdir = '/Volumes/Daltons_Archive/snowie_data/'

iop = 5
leg = 5

# start = 212710
# end = 213817

if func == 1:
	uwagi.plot_ts('cdp_lwc', iop=iop, leg=leg, indir=indir)
	plt.savefig(outdir+'iop'+str(iop)+'leg'+str(leg)+'_cdplwc_ts.png', dpi=300, bbox_inches = 'tight', pad_inches = 0.1)
	plt.show()

if func == 2:
	uwagi.plot_sd(iop=iop, leg=leg, indir=indir)
	plt.savefig(outdir+'iop'+str(iop)+'leg'+str(leg)+'_sd.png', dpi=300, bbox_inches = 'tight', pad_inches = 0.1)
	plt.show()

if func == 3:
	uwagi.plot_sd_hov(iop=iop, leg=leg, indir=indir, x_axis='space', second_var='nev_lwc')
	plt.savefig(outdir+'iop'+str(iop)+'leg'+str(leg)+'_sd_hov.png', dpi=300, bbox_inches = 'tight', pad_inches = 0.1)
	plt.show()

if func == 4:
	uwagi.sd_to_csv(iop=iop, leg=leg, indir=indir, outdir=outdir)

if func == 5:
	uwagi.sd_time_csv(iop=iop, leg=leg, indir=indir, outdir=outdir)	

if func == 6:
	uwagi.ts_to_csv(iop=iop, leg=leg, indir=indir, outdir=outdir)
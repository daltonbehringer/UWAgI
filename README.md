# UWAgI
This package provides tools to read and plot data from the University of Wyoming King Air and cloud seeding aircraft as well as track the advection of Silver Iodide from the seeding aircraft.

1. Plotting Functions (`uwagi.plot`)
   - `plot_ts` -> plots time series of given var (refer to `utility/var_labels.py` for list of vars)
   - `plot_sd` -> plots QCed size distribution
   - `plot_sd_hov` -> plots QCed size dist over time or space
   
2. Data Ingest (`uwagi.readers`)
   - `read_ka` -> reads NetCDF files from the UWKA
   - `read_seeder` -> reads csv files from the seeder aircraft
   - `read_sizedist` -> reads NetCDF files containing size distribution info from OAPs
   - `read_2DP` -> reads raw files from the 2DP probe
   - `read_2DS` -> reads raw files from the 2DS probe
   

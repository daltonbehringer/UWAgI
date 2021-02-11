# UWAgI
This package provides tools to read and plot data from the University of Wyoming King Air and cloud seeding aircraft as well as track the advection of Silver Iodide from the seeding aircraft.

1. Plotting Functions (`uwagi.plot`)
   - `plot.py`
      - `plot_ts` -> plots time series of given var (refer to `utility/var_labels.py` for list of vars)
      - `plot_sd` -> plots QCed size distribution
      - `plot_sd_hov` -> plots QCed size dist over time or space
   
2. Data Ingest (`uwagi.readers`)
   - `read_ka` -> reads NetCDF files from the UWKA
   - `read_seeder` -> reads csv files from the seeder aircraft
   - `read_sizedist` -> reads NetCDF files containing size distribution info from OAPs
   - `read_2DP` -> reads raw files from the 2DP probe
   - `read_2DS` -> reads raw files from the 2DS probe
   
3. QC and other utilities (`uwagi.utility`)
   - `csv_out.py`
      - `sd_to_csv` -> returns time-averaged size distribution in CSV format
      - `sd_time_csv` -> returns time-series size distribution in CSV format
      - `ts_to_csv` -> returns time-series of relevant UWKA vars in CSV format
   - `data_corr.py`
      - `sd_corr` -> rebins and returns size distribution info from the CDP, 2DS, and 2DP probes
      - `nev_corr` -> performs corrections for liquid, ice, and total water content from the Nevzorov probe
   - `distance.py`
      - `dist` -> calculates and returns distance from the Packer John DOW
      - `ac_dist` -> calculates and returns distance between seeder AC and UWKA
   - `iop.py`
      - `get_times` -> returns file names and IOP/leg dates and times for functions that plot or gather data based on IOP and leg number
   - `plume.py`
      - `get_plume` -> returns index of points within seeded plume
      - `get_out_plume` -> returns index of points within user-defined distance downwind of downwind-most seeded plume
 

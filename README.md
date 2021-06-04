# UWAgI
### This package provides tools to read, QC, and plot data from the University of Wyoming King Air and cloud seeding aircraft.

##### - Data Access
   - [UW King Air 1-second aircraft data](http://flights.uwyo.edu/projects/snowie17/order_1hz.shtml)
   - [UW King Air Size Spectra data](https://doi.org/10.5065/D6GT5KXK)
   - [UW King Air Manually Corrected Nevzorov data](https://doi.org/10.26023/2QRK-XSBA-RS0P)
   - [SNOWIE '17 dataset master list](https://data.eol.ucar.edu/master_lists/generated/snowie/)

##### 1. Plotting Functions ([`uwagi.plot`](https://github.com/daltonbehringer/UWAgI/tree/master/uwagi/plot))
   - [`plot.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/plot/plot.py)
      - `plot_ts` -> plots time series of given var (refer to `utility/var_labels.py` for list of vars)
      - `plot_sd` -> plots QC'ed size distribution
      - `plot_sd_hov` -> plots QC'ed size dist over time or space
   
##### 2. Data Ingest ([`uwagi.readers`](https://github.com/daltonbehringer/UWAgI/tree/master/uwagi/readers))
   - [`read_ka.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/readers/read_ka.py) -> reads NetCDF files from the UWKA
   - [`read_seeder.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/readers/read_seeder.py) -> reads csv files from the seeder aircraft
   - [`read_sizedist.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/readers/read_sizedist.py) -> reads NetCDF files containing size distribution info from OAPs
   - [`read_2DP.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/readers/read_2DP.py) -> reads raw files from the 2DP probe
   - [`read_2DS.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/readers/read_2DS.py) -> reads raw files from the 2DS probe
   
##### 3. QC and other utilities ([`uwagi.utility`](https://github.com/daltonbehringer/UWAgI/tree/master/uwagi/utility))
   - [`csv_out.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/utility/csv_out.py)
      - `sd_to_csv` -> returns time-averaged size distribution in CSV format
      - `sd_time_csv` -> returns time-series size distribution in CSV format
      - `ts_to_csv` -> returns time-series of relevant UWKA vars in CSV format
   - [`data_corr.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/utility/data_corr.py)
      - `sd_corr` -> rebins and returns size distribution info from the CDP, 2DS, and 2DP probes
      - `nev_corr` -> performs corrections for liquid, ice, and total water content from the Nevzorov probe
   - [`distance.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/utility/distance.py)
      - `dist` -> calculates and returns distance from the Packer John DOW
      - `ac_dist` -> calculates and returns distance between seeder AC and UWKA
   - [`iop.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/utility/iop.py)
      - `get_times` -> returns file names and IOP/leg dates and times for functions that plot or gather data based on IOP and leg number
   - [`plume.py`](https://github.com/daltonbehringer/UWAgI/blob/master/uwagi/utility/plume.py)
      - `get_plume` -> returns index of points within seeded plume
      - `get_out_plume` -> returns index of points within user-defined distance downwind of downwind-most seeded plume
 
 ##### 4. QC Scripts ([`uwagi.qc_scripts`](https://github.com/daltonbehringer/UWAgI/tree/master/uwagi/qc_scripts))
   - Scripts used to aid in the quality control of data from the Nevzorov probe for liquid, total, and ice water content. These will allow the user to look closely at the data to make neccessary manual corrections to the Nevzorov data. Existing corrections that have been applied already can be found via the links in `uwagi.data_corr.nev_corr()`.

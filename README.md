# Geneva Summer 2026

Analysis of Lake Geneva observations collected during summer 2026, including
meteorological, CTD, and chlorophyll data.

## Repository

- Repository root: `.`
- Remote: [GitHub repository](https://github.com/mepLAKES/Geneva_summer_2026)

## Repository Structure

All paths below are relative to the repository root (`.`):

```text
data/
	léxplorectdprofiles_datalakesdownload/
	léxploremeteostation_datalakesdownload (2)/
graphs/                 Generated figures
notebooks/              Reproducible analyses
results/                Generated CSV files
Illustrations/          Presentation and media assets
wind_climatology.py     Standalone NetCDF wind analysis
```

The uploaded NetCDF source files belong in the matching directories under `data/`.
Keep generated CSV files in `results/` and generated figures in `graphs/`.
Do not replace these repository-relative paths with absolute paths from your
local computer.

## Getting Started

1. Clone the repository and change into it:

	```sh
	git clone https://github.com/mepLAKES/Geneva_summer_2026.git
	cd Geneva_summer_2026
	```

2. Install the Python dependencies used by the analyses:

	```sh
	python -m pip install matplotlib netCDF4 numpy pandas
	```

3. Open a notebook from `notebooks/` with the repository root as its working
	directory. The notebooks resolve inputs from `data/` and outputs to
	`results/` or `graphs/` using relative paths.

### Standalone Wind Analysis

Run this command from the repository root:

```sh
python wind_climatology.py
```

It reads NetCDF files from
`data/léxploremeteostation_datalakesdownload (2)/`, then writes
`results/geneva_wind_speed_climatology.csv` and
`graphs/geneva_wind_speed_climatology.png`.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from netCDF4 import Dataset, num2date


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data" / "léxploremeteostation_datalakesdownload (2)"
RESULTS_DIR = PROJECT_DIR / "results"
GRAPHS_DIR = PROJECT_DIR / "graphs"
OUTPUT_CSV = RESULTS_DIR / "geneva_wind_speed_climatology.csv"
OUTPUT_PNG = GRAPHS_DIR / "geneva_wind_speed_climatology.png"


def load_station_data() -> pd.DataFrame:
    nc_paths = sorted(DATA_DIR.glob("*.nc"))
    if not nc_paths:
        raise FileNotFoundError(f"No NetCDF files found in {DATA_DIR}")

    frames = []
    for path in nc_paths:
        with Dataset(path) as source:
            missing = [
                name for name in ("time", "WS", "WS_qual")
                if name not in source.variables
            ]
            if missing:
                raise ValueError(f"{path.name} is missing {missing}")

            time_var = source.variables["time"]
            frame = pd.DataFrame(
                {
                    "timestamp": num2date(
                        time_var[:],
                        time_var.units,
                        only_use_cftime_datetimes=False,
                    ),
                    "wind_speed_m_s": source.variables["WS"][:],
                    "wind_quality_flag": source.variables["WS_qual"][:],
                }
            )
        frames.append(frame[["timestamp", "wind_speed_m_s", "wind_quality_flag"]])

    data = pd.concat(frames, ignore_index=True)
    data["timestamp"] = pd.to_datetime(data["timestamp"], utc=True)
    data["wind_speed_m_s"] = pd.to_numeric(data["wind_speed_m_s"], errors="coerce")
    data["wind_quality_flag"] = pd.to_numeric(data["wind_quality_flag"], errors="coerce")
    data = data[
        (data["wind_quality_flag"] == 0)
        & data["wind_speed_m_s"].notna()
        & (data["wind_speed_m_s"] >= 0)
    ].copy()
    return data.drop_duplicates(subset="timestamp").sort_values("timestamp")


def make_daily_data(data: pd.DataFrame) -> pd.DataFrame:
    daily = (
        data.set_index("timestamp")
        .resample("D")["wind_speed_m_s"]
        .agg(daily_mean="mean", observations="count")
        .dropna(subset=["daily_mean"])
        .reset_index()
    )
    daily["year"] = daily["timestamp"].dt.year
    daily["day_of_year"] = daily["timestamp"].dt.dayofyear
    return daily


def make_climatology(daily: pd.DataFrame) -> pd.DataFrame:
    climatology = (
        daily.groupby("day_of_year")["daily_mean"]
        .agg(climatology_mean="mean", climatology_std="std", years_observed="count")
        .reset_index()
    )
    return climatology


def make_plot(daily: pd.DataFrame, climatology: pd.DataFrame) -> None:
    figure, axis = plt.subplots(figsize=(13, 7), dpi=160)
    axis.plot(
        climatology["day_of_year"],
        climatology["climatology_mean"],
        color="#176b87",
        linewidth=2.4,
        label="Climatology (daily mean)",
    )
    axis.fill_between(
        climatology["day_of_year"],
        climatology["climatology_mean"] - climatology["climatology_std"],
        climatology["climatology_mean"] + climatology["climatology_std"],
        color="#8ec9d8",
        alpha=0.28,
        label="±1 standard deviation",
    )

    year_2026 = daily[daily["year"] == 2026]
    axis.plot(
        year_2026["day_of_year"],
        year_2026["daily_mean"],
        color="#d1495b",
        linewidth=1.5,
        label="2026 daily mean",
    )

    axis.set_title("Geneva wind-speed climatology with 2026 overlay")
    axis.set_xlabel("Day of year")
    axis.set_ylabel("Daily mean wind speed (m s$^{-1}$)")
    axis.set_xlim(1, 366)
    axis.grid(True, alpha=0.22)
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(OUTPUT_PNG, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    GRAPHS_DIR.mkdir(exist_ok=True)
    observations = load_station_data()
    daily = make_daily_data(observations)
    climatology = make_climatology(daily)
    result = climatology.merge(
        daily[daily["year"] == 2026][["day_of_year", "daily_mean"]].rename(
            columns={"daily_mean": "wind_speed_2026_daily_mean"}
        ),
        on="day_of_year",
        how="outer",
    ).sort_values("day_of_year")
    result.to_csv(OUTPUT_CSV, index=False)
    make_plot(daily, climatology)

    print(f"Accepted observations: {len(observations):,}")
    print(f"Daily means: {len(daily):,}")
    print(f"Years: {daily['year'].min()}-{daily['year'].max()}")
    print(f"2026 daily means: {(daily['year'] == 2026).sum():,}")
    print(f"Wrote {OUTPUT_CSV.name}")
    print(f"Wrote {OUTPUT_PNG.name}")


if __name__ == "__main__":
    main()
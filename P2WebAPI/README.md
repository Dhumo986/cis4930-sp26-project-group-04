# Automated Data Pipeline from Web APIs

Course: CIS 4930 (Spring 2026)  
Group: 04

## Group Members

| Name | FSU ID |
|---|---|
| Thomas Schmidt | tns23@fsu.edu |
| Imran Ahmed | ia24c@fsu.edu |
| Dhruv Upadhyay | dtu24@fsu.edu |

## Project Title

Florida City Weather Snapshot Pipeline (Open-Meteo)

## Project Description

This project automates weather data collection for multiple Florida cities using the Open-Meteo public API. Each run fetches current weather snapshots, handles HTTP failures gracefully, and appends records to local CSV and SQLite outputs so the dataset grows over time for analysis and reporting.

## API Documentation

- Open-Meteo API docs: https://open-meteo.com/en/docs
- Forecast endpoint used: https://api.open-meteo.com/v1/forecast

## API Justification

Open-Meteo is a strong fit for this project because it is free, public, and returns clean JSON without requiring authentication. It supports query-parameter based requests (`latitude`, `longitude`, and selected weather fields), making it ideal for demonstrating robust HTTP usage and repeated calls across multiple locations.

### API Constraints

- No API key required (easy classroom setup).
- Data is request-driven per location, so repeated calls are needed for each city.
- Must validate response content because some fields can be missing depending on requested variables.

## Data Pipeline Goals

1. Fetch weather snapshots for at least 3 cities per run.
2. Parse JSON safely and extract at least 5 meaningful fields.
3. Convert records into a `pandas.DataFrame` with clear column names.
4. Append results to a persistent CSV and SQLite table (no silent overwrite).
5. Log run status and errors to both terminal output and a file in `logs/`.

## Code Structure

Current implementation under [P2WebAPI](P2WebAPI):

```text
P2WebAPI/
├── README.md
├── api_client.py         # API calls + repeated city loop + request handling
├── pipeline.py           # Orchestrates fetch -> storage -> logging
├── storage.py            # DataFrame conversion + CSV/SQLite append logic
└── logs/
		└── .gitkeep          # keeps logs directory tracked in git
```

Output files are written to the project data folder:

- CSV: `data/processed/weather_data.csv`
- SQLite DB: `data/processed/weather_data.db`
- Log file: `logs/pipeline.log` (created at runtime)

## Storage Details

### CSV Output

The pipeline appends rows to `data/processed/weather_data.csv` each run.

- If file does not exist: writes header + rows.
- If file exists: appends only new rows (header omitted).

### SQLite Output

The pipeline appends rows to table `weather_records` in `data/processed/weather_data.db`.

- Uses `DataFrame.to_sql(..., if_exists="append")`.
- Table is auto-created on first run.

### SQLite Schema (logical)

SQLite columns are derived from DataFrame columns in each record. Typical schema fields include:

- `run_timestamp` (TEXT)
- `city` (TEXT)
- `latitude` (REAL)
- `longitude` (REAL)
- `temperature_2m` (REAL)
- `relative_humidity_2m` (REAL)
- `wind_speed_10m` (REAL)
- `weather_code` (INTEGER)
- `observation_time` (TEXT)

Example table creation shape:

```sql
CREATE TABLE weather_records (
	run_timestamp TEXT,
	city TEXT,
	latitude REAL,
	longitude REAL,
	temperature_2m REAL,
	relative_humidity_2m REAL,
	wind_speed_10m REAL,
	weather_code INTEGER,
	observation_time TEXT
);
```

## Running the Pipeline

From the repository root:

```bash
python P2WebAPI/pipeline.py
```

or from [P2WebAPI](P2WebAPI):

```bash
python pipeline.py
```

## Logging Setup

`pipeline.py` configures logging to:

- console (`StreamHandler`) for live feedback
- file (`FileHandler`) at `logs/pipeline.log`

The directory is created automatically with:

- `os.makedirs("logs", exist_ok=True)`

Repository tracking for `logs/` is enabled by committing `logs/.gitkeep`.

## Example Cron Schedule

Run every day at 8:00 AM:

```cron
0 8 * * * /usr/bin/python3 /home/imran/Repositories/cis4930-sp26-project-group-04/P2WebAPI/pipeline.py >> /home/imran/Repositories/cis4930-sp26-project-group-04/P2WebAPI/logs/cron.log 2>&1
```

## Example Run Notes

```text
[INFO] Pipeline run started
[INFO] Fetching weather data for 4 cities...
[INFO] Successfully fetched N records.
[INFO] Appended N rows to CSV.
[INFO] Appended N rows to SQLite table weather_records.
[INFO] Pipeline run completed successfully.
```


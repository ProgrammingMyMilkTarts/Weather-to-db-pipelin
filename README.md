# Automated Weather ETL & Time-Series Analytics Pipeline

A lightweight, production-style backend automation pipeline that extracts live meteorological data via an API, parses it, logs it locally, and performs time-series analytics using Python and Pandas.

## Project Overview
Mimics a mini-ETL (Extract, Transform, Load) pipeline running locally in a Linux environment, then fetches the data and uses it for analytical usage.

## Tech Stack
* **Language:** Python 3
* **Automation:** Linux Cron (Task Scheduler)
* **Data Processing & Analysis:** Pandas, CSV
* **API Integration:** OpenWeather Map API (`requests` library)
* **Version Control:** Git & GitHub

## Pipeline Architecture
1. **Extract:** A cron-scheduled worker script requests live JSON data from the OpenWeather API.
2. **Transform:** The script strips out unnecessary metadata, converts Kelvin to Celsius, formats timestamps, and structures the payload.
3. **Load:** Automatically appends clean, tabular records to a historical CSV data file (with automated header generation if the file doesn't exist).
4. **Analyze:** A secondary Pandas script processes the time-series dataset to surface rolling trends, moving averages, and global meteorological extremes.

---

## Automation Setup (Linux Cron)
The data ingestion script is fully automated using Linux Cron, executing multiple times a day (at noon and 8:00 PM) to build a dataset without manual intervention:

```bash
0 12,20 * 8-10 * /usr/bin/python3 /path/to/your/weather_script.py

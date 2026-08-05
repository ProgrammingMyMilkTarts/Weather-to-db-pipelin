# Automated Weather Data Pipeline and CLI Analyzer

A lightweight Python pipeline that pulls weather data via an API, logs it into a local CSV, and provides a command-line tool to analyze and visualize trends.

## What it does
* **Automated Data Logging:** Fetches live weather metrics (Temperature in C/K, Wind Speed, Humidity) and saves them with timestamps.
* **Data Cleaning:** Uses Pandas to fill in any missing gaps using linear interpolation.
* **CLI:** Run quick statistical summaries or generate visual graphs 

## Tech Stack
* **Language:** Python 3
* **CLI:** USed Argparse for the CLI
* **Automation:** Linux Cron (Task Scheduler)
* **Data Processing & Analysis:** Pandas, CSV, matplotlab
* **Version Control:** Git & GitHub

---

## Explination of scripts
Weather_script.py fetched current weather --> appends raw row to the weather_data.csv. (if data is missed it will leave a gap but the analyssi script will fill in gap with interpolate)

Analyze_weather.py: Loads the csv ->detects missing gaps -. runs linear interpolation -> plots charts and metrcs

## Automation Setup (Linux Cron)
The data ingestion script is fully automated using Linux Cron, executing everyhour to build a dataset without manual intervention:

```bash
10 * * * * /usr/bin/python3 /path/tothescript/weather_script.py

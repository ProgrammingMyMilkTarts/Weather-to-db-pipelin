import os
import pandas as pd
import matplotlib as plt

BASE_DIR = "/home/poppingmybooty20/Desktop/DevWork/WeatherAPIProject/Weather-to-db-pipelin"
file_path = os.path.join(BASE_DIR, "weather_data.csv")

# check if file exists then will try to load and check data 
# for if there is missing data then will use interpolation to populate missing data
if os.path.isfile(file_path):
    try:
    # 1. Load data with timestamp as the index
        df = pd.read_csv(file_path, parse_dates=["Timestamp"], index_col="Timestamp")
        print("--- RAW DATA LOADED SUCCESSFULLY ---")

        # 2. Separate numeric columns from text columns
        df_numeric = df.select_dtypes(include=["number"])

        # 3. Resample(builds a strict timeline) and interpolate
        df_resampled = df_numeric.resample("h").mean().interpolate(method="linear")

        print("--- DATA CLEANED & INTERPOLATED ---")
        print(f"Total rows after resampling: {len(df_resampled)}")

        if "Temperature (C)" in df_resampled.columns:
            print("\nSummary Statistics (Temperature Celsius):")         
            print(df_resampled["Temperature (C)"].describe())



    except Exception as e:
        print(f"An error has occured: {e}")
else:
    print(f"There is an error with the file {file_path}")


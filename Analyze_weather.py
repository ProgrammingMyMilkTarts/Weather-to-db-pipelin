import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import numpy as np


#setting up arguments + read flags from terminal
parser = argparse.ArgumentParser(description="Analyze and see weather logs")
parser.add_argument("--summary",action="store_true",help="Print summary of data")
parser.add_argument("--plot",type=str,choices = ["tempC","tempK","wind","humidity","dual"],help = "plot specific metric: tempC,tempF,wind,humidity")
parser.add_argument("--daily", action ="store_true",help="Resample and change the time data from hours to days")

args = parser.parse_args()

#file path setup
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
        if(args.daily):
            df_resampled = df_numeric.resample("D").mean().interpolate(method="linear")
            time_label = "Daily Average"
        else:
            df_resampled = df_numeric.resample("h").mean().interpolate(method="linear")
            time_label = "Hourly Average"

        #handle --summary flag
        if args.summary:
            print(f"\nWeather Data Summary ({time_label.upper()})\n")
            print(df_resampled.describe())

        #handling --plot flat for tempC , tempK, wind speed, humidity
        if args.plot == "tempC":
            if "Temperature (C)" in df_resampled.columns:
                plt.figure(figsize = (10,5))
                plt.plot(df_resampled.index,df_resampled["Temperature (C)"],color = "orange",linewidth = 2)
                plt.title(f"{time_label} Temperature Trend")
                plt.xlabel("Timestamp")
                plt.ylabel("Temperature (C)")
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: Temperature (C) column not found")

        elif args.plot == "tempK":
            if "Temperature (K)" in df_resampled.columns:
                plt.figure(figsize = (10,5))
                plt.plot(df_resampled.index,df_resampled["Temperature (K)"],color = "orange",linewidth = 2)
                plt.title(f"{time_label} Temperature Trend")
                plt.xlabel("Timestamp")
                plt.ylabel("Temperature (K)")
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: Temperature (K) column not found")

        elif args.plot == "wind":
            if "Wind Speed (m/s)" in df_resampled.columns:
                plt.figure(figsize = (10,5))
                plt.plot(df_resampled.index,df_resampled["Wind Speed (m/s)"],color = "orange",linewidth = 2)
                plt.title(f"{time_label} Windy Trend")
                plt.xlabel("Timestamp")
                plt.ylabel("Wind Speed (m/s)")
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: Wind Speed (m/s) column not found")

        elif args.plot == "humidity":
            if "Humidity (%)" in df_resampled.columns:
                plt.figure(figsize = (10,5))
                plt.plot(df_resampled.index,df_resampled["Humidity (%)"],color = "orange",linewidth = 2)
                plt.title(f"{time_label} Humidity Trend")
                plt.xlabel("Timestamp")
                plt.ylabel("Humidity (%)")
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: Humidity (%) column not found")

        elif args.plot == "dual":
            if "Temperature (C)" in df_resampled.columns and "Wind Speed (m/s)" in df_resampled.columns:
                #create dual axis
                fig,ax1 = plt.subplots(figsize = (10,5))

                #temp axis
                color = "tab:red"
                ax1.plot(df_resampled.index,df_resampled["Temperature (C)"],color = "orange",linewidth = 2)
                ax1.set_xlabel("Timestamp")
                ax1.set_ylabel("Temperature (C)", color=color)  
                ax1.grid(True)
                ax1.tick_params(axis="y", labelcolor=color)

                #wind speed
                ax2 = ax1.twinx()
                color = "tab:blue"
                ax2.set_ylabel("Wind Speed", color=color)
                ax2.plot(df_resampled.index, df_resampled["Wind Speed (m/s)"], color=color,linestyle="--",marker="x",label="Wind Speed")
                ax1.tick_params(axis="y", labelcolor=color)

                plt.title(f"{time_label} Temperature vs. Wind Speed")
                plt.xticks(rotation = 45)
                plt.tight_layout()
                plt.show()

            else:
                print("Error: Wind speed or temperature not found column not found")


        if not args.summary and not args.plot:
                print("--- DATA CLEANED & INTERPOLATED ---")
                print(f"Total rows after resampling: {len(df_resampled)}")

    except Exception as e:
        print(f"An error has occured: {e}")
else:
    print(f"There is an error with the file {file_path}")


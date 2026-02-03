# Frozen!
import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/IOT-temp.csv")

# 08-12-2018 09:30
print(df["noted_date"])
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

range_max = df["noted_date"].max()
range_min = range_max - dt.timedelta(days=7)

sliced_df = df[(df["noted_date"] >= range_min) & (df["noted_date"] <= range_max)]

out_temp = df[(df["out/in"] == "Out")]
in_temp = df[(df["out/in"] == "In")]

plt.plot(out_temp["noted_date"].values, out_temp["temp"].values, label="Out")
plt.plot(in_temp["noted_date"].values, in_temp["temp"].values, label="In")
plt.legend(loc="best")
plt.xlabel("Time [date]")
plt.ylabel("Temperature [°C]")
plt.grid()
plt.show()


def insideout(row, fstr):
    return 1 if row["out/in"] == fstr else 0


def get_date(row):
    dt_obj = row["noted_date"]
    return f"{dt_obj.day}-{dt_obj.month}-{dt_obj.year}"


def get_hour(row):
    dt_obj = row["noted_date"]
    return f"{dt_obj.hour}:{dt_obj.minute}"


df["Out"] = df.apply(lambda row: insideout(row, "Out"), axis=1)
df["In"] = df.apply(lambda row: insideout(row, "In"), axis=1)

df["Date"] = df.apply(lambda row: get_date(row), axis=1)
df["Time"] = df.apply(lambda row: get_hour(row), axis=1)

range_max = df["noted_date"].max()
range_min = range_max - dt.timedelta(days=1)

one_day_df = df[(df["Date"] == "8-12-2018")]

print(one_day_df)
one_day_df.to_csv("./data/iot-temp-processed.csv", index=False)

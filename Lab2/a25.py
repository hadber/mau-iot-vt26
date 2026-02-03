import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/Climate2016.csv")


def vectorize(row, trig):
    velocity = row["windvelo (m/s)"]
    degrees = row["winddeg (deg)"]
    return velocity * trig(degrees)


df["Wind X"] = df.apply(lambda row: vectorize(row, math.cos), axis=1)
df["Wind Y"] = df.apply(lambda row: vectorize(row, math.sin), axis=1)

df.to_csv("./data/wind.csv", index=False)

df2 = df[["Wind X", "Wind Y"]]
df = df[["windvelo (m/s)", "winddeg (deg)"]]

normalized_df = (df - df.min()) / (df.max() - df.min())
normalized_df2 = (df2 - df2.min()) / (df2.max() - df2.min())

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Gone with the Wind")

h1 = ax1.hist2d(df["winddeg (deg)"], df["windvelo (m/s)"], bins=[50, 50], vmax=400)
ax1.set(xlabel="Wind Direction [deg]", ylabel="Wind Velocity [m/s]")
fig.colorbar(h1[3], ax=ax1)

h2 = ax2.hist2d(df2["Wind X"], df2["Wind Y"], bins=[50, 50], vmax=400)
ax2.set(xlabel="Wind X [m/s]", ylabel="Wind Y [m/s]")
fig.colorbar(h2[3], ax=ax2)

plt.show()

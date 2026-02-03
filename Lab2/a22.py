import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# for timestamp - we know when we started so we can
# just keep increasing every row by
# start + timestamp * delay

df = pd.read_csv("./data/move.csv")

names = df.columns.values[1:]
df.drop("Timestamp", axis=1, inplace=True)
values = df.values

df_filtered = df[~((df >= -200) & (df <= 200)).all(axis=1)]
new_values = df_filtered.values

# change between values and new_values for different graphs
plt.plot(new_values, label=names)
plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration ($m^2/s^2$)")
plt.grid()
plt.legend(loc="upper right")
plt.show()

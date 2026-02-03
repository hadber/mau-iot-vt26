import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/temperature_float.csv")

# names = df.columns.values
values = [x[1] for x in df.values]

# noisy data but we can clearly see an increase in temperature :)
plt.plot(values, c="orange", label="Temperature")
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.legend(loc="upper right")
plt.show()

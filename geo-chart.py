import pandas as pd
import time

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import numpy as np
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

data = pd.read_csv("5g_coverage.csv")
data.info()

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))
ax.stock_img()

ax.set_global()
ax.coastlines()

ax.set_xticks(np.arange(-180, 180, 40), crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.grid()

ax.spines["bottom"].set_visible(True)
ax.spines["left"].set_visible(True)
ax.spines["right"].set_visible(True)
ax.spines["top"].set_visible(True)
ax.spines["bottom"].set_linewidth(2.5)
ax.spines["left"].set_linewidth(2.5)
ax.spines["right"].set_linewidth(2.5)
ax.spines["top"].set_linewidth(2.5)


t1 = time.time()  # start time
for index, row in data.iterrows():
    ax.plot(
        row["longitude"],
        row["latitude"],
        "v",
        color="r",
        markersize=2,
        transform=ccrs.PlateCarree(),
    )
print(time.time() - t1)  # end time
ax.set_xlabel("Longitude", size=20)
ax.set_ylabel("Latitude", size=20)
ax.set_title("5G-covered Cities On World Map", size=30)
plt.show()

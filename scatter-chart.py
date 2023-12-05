import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import cartopy.crs as ccrs


data = pd.read_csv("5g_coverage.csv")

topN = ["AT&T Mobility", "Verizon Wireless", "T-Mobile"]
filtdata = data[data["operator"].isin(topN)]
filtdata = filtdata.reset_index(drop=True)
filtdata.info()

verizon = filtdata[filtdata["operator"] == "Verizon Wireless"]
att = filtdata[filtdata["operator"] == "AT&T Mobility"]
tmobile = filtdata[filtdata["operator"] == "T-Mobile"]


fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))
ax.scatter(
    verizon["longitude"],
    verizon["latitude"],
    marker="o",
    facecolors="none",
    color="r",
    alpha=0.7,
    lw=0.3,
    s=6,
    label="AT&T Mobility",
    transform=ccrs.PlateCarree(),
)
ax.scatter(
    att["longitude"],
    att["latitude"],
    marker="^",
    facecolors="none",
    color="#1E90FF",
    alpha=0.7,
    lw=0.3,
    s=6,
    label="Verizon Wireless",
    transform=ccrs.PlateCarree(),
)
ax.scatter(
    tmobile["longitude"],
    tmobile["latitude"],
    marker="v",
    facecolors="none",
    color="g",
    alpha=0.7,
    lw=0.3,
    s=6,
    label="T-Mobile",
    transform=ccrs.PlateCarree(),
)
ax.set_extent([-128, -62, 23, 52], crs=ccrs.PlateCarree())
ax.legend()
ax.set_xlabel("Longitude", size=20)
ax.set_ylabel("Latitude", size=20)
ax.set_title("5G Distribution Of The Three Major U.S. Carriers", size=30)

plt.show()

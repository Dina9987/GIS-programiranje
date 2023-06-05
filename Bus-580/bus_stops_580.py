import time

import geopandas as gpd
import matplotlib.pyplot as plt
import keyboard
from shapely import LineString

def on_key_press(event):
    if event.name == 'p':
        Vreme_tekst = ax.text(0.01, 0.95, "Vreme : ", transform=ax.transAxes, fontsize=6, verticalalignment='top')
        Ime_tekst = ax.text(0.01, 0.92, "Naziv stanice : ", transform=ax.transAxes, fontsize=6, verticalalignment='top')

        for geometry, stanica, vreme, ime in zip(trasa_shapefile['geometry'], trasa_shapefile['Stanica'], trasa_shapefile['Vreme'], trasa_shapefile['Ime stanic']):
            linestring = LineString(geometry)
            gs_linestring = gpd.GeoSeries([linestring])
            gs_linestring.plot(ax=ax, color='orange', linewidth=2)

            if stanica == 1:
                Vreme_tekst.set_text("Vreme : "+vreme)
                Ime_tekst.set_text("Naziv stanice : "+ime)

            plt.draw()
            time.sleep(0.2)
        ax.text(0.01, 0.89, "Duzina puta : 60.4km", transform=ax.transAxes, fontsize=6, verticalalignment='top')
        plt.draw()

opstine_shapefile = gpd.read_file("shp_files/Beogradske opstine.shp")
trasa_shapefile = gpd.read_file("shp_files/Novi put.shp")
stanice_shapefile = gpd.read_file("shp_files/STanice.shp")

keyboard.on_press(on_key_press)

fig, ax = plt.subplots(figsize=(15,15))

opstine_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')
stanice_shapefile.plot(ax=ax, color='blue', markersize=10)

point_counter = 1
x_offset = 1
y_offset = 3
for x,y,label in zip(stanice_shapefile.geometry.x, stanice_shapefile.geometry.y, stanice_shapefile['Naziv']):
    if point_counter == 2 or point_counter == 6:
        y_offset = -2
    ax.annotate(point_counter, xy=(x,y), xytext=(x_offset,y_offset), textcoords="offset points", color='blue')
    point_counter=point_counter+1
    x_offset = 3
    y_offset = 3

ax.text(0.01, 0.98, "Trasa autobusa 580", transform=ax.transAxes, fontsize = 6, verticalalignment='top')

plt.show()

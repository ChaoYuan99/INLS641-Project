import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import folium
from folium import plugins
import io
from PIL import Image
from selenium import webdriver
import time

df = pd.read_csv('C:/Users/ycapp/Desktop/All_cases_by_modzcta.csv')
print(df)

#Separeted only the coordinates and cases
coordinates = df[['latitude' , 'longitude', 'cases']]
test_cord = coordinates[0:177]


#creating the map using <folium>
baseMap = folium.Map(
                width="100%",
                height="100%",
                location=[40.71250, -74.00000],
                zoom_start=11
)

#Drawing the heatmap on the map selected
baseMap = baseMap.add_child(folium.plugins.HeatMap(test_cord))

baseMap.save('C:/temp/All_cases_by_modzcta.html')
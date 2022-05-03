import pandas as pd
import numpy as np
import folium
from folium import plugins


df = pd.read_csv('C:/Users/ycapp/Desktop/diff_region ( Dec and Jan ).csv')
print(df)

#Separeted only the coordinates and cases
coordinates = df[['latitude' , 'longitude', 'Cases']]
test_cord = coordinates[0:5]


#creating the map using <folium>
baseMap = folium.Map(
                width="100%",
                height="100%",
                location=[40.71250, -74.00000],
                zoom_start=11
)

#Drawing the heatmap on the map selected
baseMap = baseMap.add_child(folium.plugins.HeatMap(test_cord))


#Creating a circle with the information about the cases in the neighborhood
for i in range(5):
    folium.Circle(
        location = (df.iloc[i]['latitude'], df.iloc[i]['longitude']),
        color   = '#8000ff',
        # #00FF69
        #fill    = '#00A1B3',
        tooltip = '<li><bold> County:' + str(df.iloc[i]['County']) +
                  '<li><bold> Cases: ' + str(df.iloc[i]['Cases']),
        radius  = (df.iloc[i]['Cases']**0.75)
    ).add_to(baseMap)



baseMap.save('C:/temp/diff_region ( Dec and Jan ).html')
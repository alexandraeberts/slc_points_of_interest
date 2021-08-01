#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 12:57:17 2021

@author: alexeberts
"""
import geopandas as gpd
import folium
import pandas as pd

slc = folium.Map(location = [40.7608, -111.8910], tiles = 'openstreetmap', zoom_start = 10)
slc.save('slc.html')

poi = pd.read_csv('poi.csv')
poi

trip = gpd.GeoDataFrame(poi, geometry = gpd.points_from_xy(poi.Longitude, poi.Latitude))
trip.crs = 'EPSG:4326'
trip.crs
trip.info()

def color_producer(Type):
    if Type == 'Restaurant':
        return 'red'
    elif Type == 'Bakery':
        return 'blue'
    elif Type == 'Stay':
        return 'black'
    elif Type == 'Brewery':
        return 'pink'
    elif Type == 'Boat Rental':
        return 'orange'
    else:
        return 'green'

def radius_producer(Interest_Level):
    if Interest_Level >= 7:
        return 10
    else:
        return 5

for i in range(0,len(trip)):
    folium.CircleMarker(
        location=[trip.iloc[i]['Latitude'], trip.iloc[i]['Longitude']],
        popup = ("{}, {}").format(trip.iloc[i]['Name'],
                                    trip.iloc[i]['Notes']),
        color = color_producer(trip.iloc[i]['Type']), 
        radius = radius_producer(trip.iloc[i]['Interest_Level']),
        fill = True).add_to(slc)

slc.save('slc.html')

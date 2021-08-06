#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:30:40 2021

@author: alexeberts
"""

"""
Function to determine itinerary
"""

import pandas as pd
import geopandas as gpd

points = pd.read_csv('poi.csv')
points
points.head()

locations = gpd.GeoDataFrame(points, geometry = gpd.points_from_xy(points.Longitude, points.Latitude))
locations.info()
print(locations.crs)
locations.crs = 'EPSG:2272'

def loc_sel(loc, t1):
    #subset by t1
    sub = locations[locations['Type'] == t1]
    distance = sub.geometry.distance(loc.geometry)
    return print(locations.iloc[distance.idxmin()][['Name']])

loc_sel(locations.iloc[9], 'Restaurant')

locations.iloc[1]
locations.iloc[5]
locations.iloc[10]
locations.iloc[9]

#input
val = input('Enter the type you are interested in searching by?\n')
print(f'You entered {val}')

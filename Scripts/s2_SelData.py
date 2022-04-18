import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely import wkt
from shapely.geometry import Point, Polygon
from shapely.wkt import loads

bdir='/home/guraylab/MUSA/Dev/GeoPandas/Data'

## Read data
gdf_NP = gpd.read_file(bdir + '/geo-data-master/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.shp')
gdf_PD = gpd.read_file(bdir + '/geo-data-master/politcal-wards-divisions/2016/2016_Ward_Divisions.shp')
gdf_LU = gpd.read_file(bdir + '/Land_Use_Phila/Land_Use.shp')

## Convert coordinate system
gdf_NP.to_crs("EPSG:4326", inplace=True)
gdf_PD.to_crs("EPSG:4326", inplace=True)

## Create a geo-dataframe `polygon_df` having 1 row of polygon
# This polygon will be used to select points in a geodataframe
d = {'poly_id':[1], 'wkt':['POLYGON ((-76 39.93, -75.15 39.93, -75.15 39.98, -76 39.98, -76 39.93))']}
d = {'poly_id':[1], 'wkt':['POLYGON ((-75.23 39.93, -75.17 39.93, -75.17 39.97, -75.23 39.97, -75.23 39.93))']}

df = pd.DataFrame(data=d)
geometry = [loads(pgon) for pgon in df.wkt]
polygon_df = gpd.GeoDataFrame(df, crs={'init': 'EPSG:4326'}, geometry=geometry)

## Restrict them to a selected region
gdf_LU = gpd.sjoin(gdf_LU, polygon_df, predicate='within', how='inner')
gdf_PD = gpd.sjoin(gdf_PD, polygon_df, predicate='within', how='inner')
gdf_NP = gpd.sjoin(gdf_NP, polygon_df, predicate='within', how='inner')

## View maps
#gdf_NP.plot('Shape_Area', legend=True, cmap='OrRd')
gdf_PD.plot('AREA_SFT', legend=True, cmap='OrRd')
#gdf_LU.plot('C_DIG1', legend=True)
plt.show()


## Merge maps
gdf_M = gpd.overlay(gdf_NP, gdf_LU, how='intersection')

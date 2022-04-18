import matplotlib.pyplot as plt
import geopandas

bdir='/home/guraylab/MUSA/Dev/GeoPandas/Data'

## Read data
gdf_NP = geopandas.read_file(bdir + '/geo-data-master/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.shp')
gdf_PD = geopandas.read_file(bdir + '/geo-data-master/politcal-wards-divisions/2016/2016_Ward_Divisions.shp')
gdf_LU = geopandas.read_file(bdir + '/Land_Use_Phila/Land_Use.shp')

## Convert coordinate system
gdf_NP.to_crs("EPSG:4326", inplace=True)
gdf_PD.to_crs("EPSG:4326", inplace=True)

## View maps
#gdf_NP.plot('Shape_Area', legend=True, cmap='OrRd')
#gdf_PD.plot('AREA_SFT', legend=True, cmap='OrRd')
gdf_LU.plot('C_DIG1', legend=True)
plt.show()

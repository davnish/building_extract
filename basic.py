import geopandas as gpd
import rasterio as rio
import matplotlib.pyplot as plt

img = rio.open('data.tif')
masks = rio.open('label.tif')

data = img.read()
masks_data = masks.read()
plt.imshow(masks_data.transpose((1,2,0)))
# plt.imshow(data.transpose((1,2,0)))
plt.show()


from PIL import Image
import numpy as np
from filter import transform_to_mosaic


file_name = "scale1200.jpg"
res_name = "res_new.jpg"
pixel_size = 10
gray_gradation = 255 // 50
img = Image.open(file_name)
img_arr = np.array(img)
transform_to_mosaic(img_arr, pixel_size, gray_gradation)
res = Image.fromarray(img_arr)
res.save(res_name)

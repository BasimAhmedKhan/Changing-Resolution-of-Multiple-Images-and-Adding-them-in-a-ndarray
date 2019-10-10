import numpy as np
import os
from PIL import Image
import glob


image_list = []
resized_image = []
arr = np.ones([20, 512, 512, 3])

for f in glob.glob(r'C:\Users\DELL\PycharmProjects\projects\im\*.jpg'):
    img = Image.open(f)
    image_list.append(img)

for im in image_list:
    res = im.resize((512, 512))
    resized_image.append(res)

i = 0
for (i, new) in enumerate(resized_image):
    new.save('{}{}{}'.format(r'C:\Users\DELL\PycharmProjects\projects\resized_image\new', i + 1, '.jpg'))

y = 0
for x in range(1, 21):
    im = Image.open("./resized_image/new" + str(x) + ".jpg")
    arr[y, :, :, :] = im
    y += 1


print(arr)


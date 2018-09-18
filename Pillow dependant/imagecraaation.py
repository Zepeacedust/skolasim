from PIL import Image
import random
im = Image.new("RGB", (255,255), color= 0)
height, width = im.size
for x in range(height):
    for y in range(width):
        im.putpixel((x, y), (y, x, y))
Image._show(im)

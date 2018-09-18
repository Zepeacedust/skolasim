from PIL import Image
im = Image.open("Spectrum.png")
width, height = im.size
Image._show(im)
for x in range(width):
    for y in range(height):
        R, G, B = im.getpixel((x, y))
        im.putpixel((x, y),(R, G ** 2, B))
Image._show(im)


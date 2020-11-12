from PIL import Image

im = Image.open('romeo1.jpg')

print(im.format, im.size, im.mode)
im.show()

#Black and white image
im.convert(mode='L').save('romeo_bw.jpg')

#im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

from PIL import Image
import os

size_300 = (300,300) #Size of the new images

#Loop over the contents of the current directory
for f in os.listdir('.'):
    #Search for all .jpg images
    if f.endswith('.jpg'):
        i = Image.open(f)
        #Slpit the filename and the file extension
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))

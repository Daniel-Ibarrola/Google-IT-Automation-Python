from PIL import Image
import os

#Loop over the contents of the current directory
for f in os.listdir('.'):
    #Search for all .jpg images
    if f.endswith('.jpg'):
        i = Image.open(f)
        #Slpit the filename and the file extension
        fn, fext = os.path.splitext(f)
        
        i.rotate(90).save('pngs/{}.png'.format(fn))

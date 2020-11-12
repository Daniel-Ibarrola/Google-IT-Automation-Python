#!/usr/bin/env python3
from PIL import Image
import os

size = (600,400) #Size of the new images
path = '/home/student-02-faee917e59b7/supplier-data/images/'

#Loop over the contents of the directory
for f in os.listdir(path):
    #print(f)
    #Search for all .tiff images
    if f.endswith('.tiff'):
        i = Image.open(os.path.join(path, f)).convert('RGB')
        #Split the filename and the file extension
        fn, fext = os.path.splitext(f)

        i.thumbnail(size)
        i.save('/home/student-02-faee917e59b7/supplier-data/images/{}.jpeg'.format(fn))

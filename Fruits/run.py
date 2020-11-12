#!/usr/bin/env python3
import os
import requests
import re

path = '/home/student-02-faee917e59b7/supplier-data/descriptions/'
pattern = r'(^\d+)'

#Traverse each file of the specified path
for f in os.listdir(path):
    fn, fext = os.path.splitext(f)
    #print(fn)
    #open each text file
    with open(os.path.join(path, f), 'r') as text:

        description = dict()
        keys = ['name','weight','description','image_name']
        keycount = 0

        #Add the data to each dictionary
        for line in text:
            line = line.rstrip()
            #Remove the lbs from the weight. Search if the line has a number.
            number = re.search(pattern, line)
            if number is not None:
                #print(number)
                line = int(number[1])

            description[keys[keycount]] = line
            keycount += 1
        #Add the corresponding image
        description['image_name'] = f'{fn}.jpeg'
    #Upload the files to the website
    r = requests.post('http://104.197.120.88/fruits/', json = description)
    print(r.request.body)
    print(r.status_code)
    #print(description)

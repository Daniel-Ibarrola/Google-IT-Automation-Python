#!/usr/bin/env python3
import os
import requests
import re

path = '/Daniel/Documents/Python/Fruits/supplier-data/descriptions/'
pattern = r'(^\d+)'

#Traverse each file of the specified path
for f in os.listdir(path):
    #open each text file
    with open(os.path.join(path, f), 'r') as text:

        description = dict()
        keys = ['name','weight','description',]
        keycount = 0

        #Add the data to each dictionary
        for line in text:
            line = line.rstrip()
            #Remove the lbs from the weight. Search if the line has a number
            number = re.search(pattern, line)
            if number is not None:
                #print(number)
                line = int(number[1])

            description[keys[keycount]] = line
            keycount += 1
    print(description)

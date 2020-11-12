#!/usr/bin/env python3
import os
import requests
import regex

path = '/Daniel/Documents/Python/Fruits/supplier-data/descriptions/'

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
            description[keys[keycount]] = line
            keycount += 1
    print(description)

#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

path = '/home/student-02-faee917e59b7/supplier-data/images/'

for f in os.listdir(path):
    #print(file)
    if f.endswith('jpeg'):
        with open(os.path.join(path, f), 'rb') as opened:
            r = requests.post(url, files={'file': opened})

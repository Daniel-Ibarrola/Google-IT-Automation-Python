#!/usr/bin/env python3
import os
import datetime
import sys
from reports import generate_report
from emails import generate_email
from emails import send_email

def process_data(files_path):
    """Process the data on each text file and creates a list to generate the report."""
    fruit_list = list()
    #Traverse each file of the specified path
    for f in os.listdir(files_path):
        with open(os.path.join(files_path, f), 'r') as text:
            line1 = text.readline()
            line2 = text.readline()
            fruit = 'name: {}'.format(line1)
            weight = 'weight: {}'.format(line2)
            #print(fruit)
            #print(weight)
            fruit_list.append(fruit)
            fruit_list.append(weight)
            fruit_list.append('\n')

    fruit_summary = '<br/>'.join(fruit_list)

    return fruit_summary

def main(argv):
    path = '/home/student-02-faee917e59b7/supplier-data/descriptions/'
    report_info = process_data(path)
    title = 'Process Update on' + ' ' + datetime.date.today().strftime("%B %d, %Y")
    generate_report('/tmp/processed.pdf',title, report_info)
    msg = generate_email('automation@example.com',
             'student-02-faee917e59b7@example.com',
             'Upload Completed - Online Fruit Store',
             'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
             '/tmp/processed.pdf')
    #print(msg)
    send_email(msg)


if __name__ == "__main__":
  main(sys.argv)

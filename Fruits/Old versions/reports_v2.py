#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os
import datetime

def generate_report(filename,title,additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title,empty_line,report_info])

path = '/Daniel/Documents/Python/Fruits/supplier-data/descriptions/'
fruit_list = list()

#Traverse each file of the specified path
for f in os.listdir(path):

    with open(os.path.join(path, f), 'r') as text:
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

title = 'Process Update on' + ' ' + datetime.date.today().strftime("%B %d, %Y")
#print(title)
#print(fruit_list)
generate_report('test.pdf',title, fruit_summary)

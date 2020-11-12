from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import json

#open and read the json file
with open('car_sales.json', 'r') as f:
    data = json.load(f)


table_data = [['ID','Car', 'Price','Total Sales']]

#traverse the data from the json file
for sale in data:
    sale_list = list()
    sale_list.append(sale['id'])
    car_details = '{} {} ({})'.format(sale['car']['car_make'], sale['car']['car_model'], sale['car']['car_year'])
    #print(car_details)
    sale_list.append(car_details)
    sale_list.append(sale['price'])
    sale_list.append(sale['total_sales'])
    #print(sale_list)
    table_data.append(sale_list)

print(table_data)

#Generate an empty pdf
report = SimpleDocTemplate("cars.pdf")
#Use the default syle
styles = getSampleStyleSheet()
#h1 represents the style for the first level of headers
report_title = Paragraph("Sales summary for last month", styles["h1"])

empty_line = Spacer(1,20)
report_info = Paragraph('''
The Mercedes generated the most revenue<br/>
The Acura had the most sales<br/>
The most popular year was 2007''')

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')

report.build([report_title,empty_line,report_info, empty_line, report_table,])

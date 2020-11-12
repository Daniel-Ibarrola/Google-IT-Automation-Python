import json

#open and read the json file
with open('car_sales.json', 'r') as f:
    data = json.load(f)

#for sale in data:
#    print(sale['id'])
#    print(sale['car']['car_make'])
#    print(sale['price'])
#    print(sale['total_sales'])

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

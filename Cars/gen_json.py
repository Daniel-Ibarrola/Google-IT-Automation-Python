import json

car_sales = [
        {
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murcielago",
                "car_year": 2002
                },
        "price": "$13724.05",
        "total_sales": 149
        },
        {
        "id": 10,
        "car": {
                "car_make": "Chevrolet",
                "car_model": "Cvalier",
                "car_year": 2004
                },
        "price": "$11020.05",
        "total_sales": 945
        },
]


#dump() method writes to a file
with open('car_sales.json', 'w') as car_json:
    json.dump(car_sales,car_json, indent=2)

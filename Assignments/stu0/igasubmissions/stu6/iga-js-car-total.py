def iga():
    car_list = [
        {
            "car_id": 1,
            "color": "red",
            "data": "Cost: 20000"
        },
        {
            "car_id": 2,
            "color": "red",
            "data": "Cost: 30000"
        },
        {
            "car_id": 3,
            "color": "yellow",
            "data": "Cost: 30000"
        }
    ]

    total = 0
    for x in car_list:
        if x['color'] == "red":
            result = int(x['data'][6:])
            total += result
            return total
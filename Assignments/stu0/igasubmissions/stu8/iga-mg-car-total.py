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

    print(calc_total_cost(car_list))


def calc_total_cost(car_list):

    redcars = [c['data'] for c in car_list if c['color'] == 'red']
    retval = 0
    for r in redcars:
        cost = int(r.replace("Cost: ", ""))
        retval += cost
    return f"Total cost: {retval}."


if __name__ == '__main__':
    iga()

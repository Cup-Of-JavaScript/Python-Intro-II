def calc_total_cost(car_list):
    retval = 0
    for i in car_list:
        retval += Int(i)
        return retval


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
    print(car_list[0]["data"]) + (car_list[1]["data"])
    print(calc_total_cost(car_list))

if __name__ == '__main__':
    iga()


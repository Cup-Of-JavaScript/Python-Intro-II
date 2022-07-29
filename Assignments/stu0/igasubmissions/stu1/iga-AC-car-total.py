def calc_total_cost(car_list):
    result = ''
    for x in car_list:
        y = car_list[1]["data"]
        car_cost_one = int(y[6:10])
        z =car_list[0]["data"]
        car_cost_two = int(z[6:10])
        return f'{"Total Cost: "}{car_cost_one + car_cost_two}'

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

if __name__ == '__main__':
    iga()



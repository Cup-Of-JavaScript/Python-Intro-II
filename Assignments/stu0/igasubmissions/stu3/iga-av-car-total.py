def calc_total_cost(car_list):
    for cars in car_list:
        print("data"[9:13])

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
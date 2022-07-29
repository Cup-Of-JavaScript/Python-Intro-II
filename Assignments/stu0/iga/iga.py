#
# File: iga.py
# Auth: Martin Burolla
# Date: 7/28/2022
# Desc: Car Cost
#

def calc_total_cost(car_list):
    total_cost = 0
    for c in car_list:
        if c["color"] == "red":
            total_cost += int(c["data"][6:])
    return f"Total cost: {total_cost}."


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

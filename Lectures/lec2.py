# Objects
# Call by value, call by reference

def temp():
    car_list = [
        {
            'make': 'toyota',
            'cost': 24000,
            'engine':
                {
                    'size': 2.0,
                    'type': 'Flat 4'
                },
        },
        {
            'make': 'ford',
            'cost': 25000,
            'engine':
                {
                    'size': 3.0,
                    'type': 'Flat 6'
                }
        }
    ]

    print(car_list[1]['cost'])



def lec2():

    temp()

    person = {
        "name": "Joe",
        "guitars": [
            {
                "model": "Suhr",
                "cost": 3000
            },
            {
                "model": "Gibson",
                "cost": 2000
            },
            {
                "model": "Fender",
                "cost": 1000
            }
        ],
        "bank_account":
            {
                "account_id": 123,
                "name": "checking"
            }
    }

    # print(person["bank_account"]["account_id"])
    # print(person["guitars"][2]["cost"])

    # guitars = person["guitars"]
    # total_cost = 0
    # for g in guitars:
    #     total_cost += g["cost"]
    # print(total_cost)



if __name__ == '__main__':
    lec2()

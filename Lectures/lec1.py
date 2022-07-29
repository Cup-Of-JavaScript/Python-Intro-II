# type()
# id()
# Equality
# https://www.w3schools.com/python/python_datatypes.asp
# For loops
# string slicing : https://www.w3schools.com/python/python_strings_slicing.asp
# input
# List & Dictionaries
# If
# While
# Casting: https://www.w3schools.com/python/python_casting.asp
# f string

def calc_sum(shopping_cart):
    retval = 0
    for i in shopping_cart:
        retval += i['price']
    return retval


def lec1():
    shopping_cart = [
        {"item_id": "1", "name": "socks", "price": 10.00},
        {"item_id": "2", "name": "boots", "price": 60.00},
        {"item_id": "3", "name": "pants", "price": 30.00}
    ]
    print(shopping_cart[0]["name"])
    print(calc_sum(shopping_cart))


if __name__ == '__main__':  # Dunder
    lec1()

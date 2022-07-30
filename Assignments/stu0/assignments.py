#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#

import requests
import psycopg2
import boto3


def ex1():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)


def ex2():
    print('here')

def ex3():
    print('here')


def ex4():
    print('here')


def ex5():
    print('here')


def ex6():
    print('here')


def ex7():
    print('here')


def ex8():
    print('here')


def ex9():
    print('here')


#
# Place your functions here...
#

def sort_people(people, field, direction):
    people.sort(key=lambda p: p[field], reverse=False if direction == "asc" else True)
#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python II
#

#import requests
#import psycopg2
#from psycopg2 import pool
#import logging
#import boto3
#import time
#from datetime import datetime

#sqs = boto3.client('sqs')
#INSERT_CAT = ""
#SELECT_CAT = ""

#pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                            #user="postgres",
                                           #password="Ihgdp51505150!",
                                            #host="localhost",
                                           #database="Cats")


def ex1():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    #sort_people(people_list, 'weight', 'desc')
    #print(people_list)


def ex2():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    #filtered_list = filter_males(people_list)
    #print(filtered_list)



def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'ssn': '111-11-1111'},
        {'id': 3, 'name': 'charlie', 'ssn': '222-22-2222'},
    ]
    new = calc_ssn(people_list)
    print(new)



def ex4():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))


def ex5():
    print("TODO ...")

def ex6():
    print("TODO ...")
    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    # save_to_cat_table(cat)


def ex7():
    print("TODO ...")
    cat_id = 1
    # cat = get_cat(cat_id)
    # print(cat)


#
# Place your functions here...
#





def get_people(people_list):

    l = [p['name'] for p in people_list if p['age'] >= 15]
    return l

def calc_ssn(people_list):
    list_ssn = list(map(lambda p: {
        'id': p['id'],
        'name': p['name'],
        'ssn': p['ssn'][7:]
    },  people_list))
    return list_ssn

def filter_males(people_list):

    return list(filter(lambda p : p['sex'] == 'male', people_list))

def sort_people(people_list, a, b):
    if b == "desc":
        people_list.sort(key = lambda x: x[a], reverse = True)
    else:
        people_list.sort(key = lambda x: x[a])


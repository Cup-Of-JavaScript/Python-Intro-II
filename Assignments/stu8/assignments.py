#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python II
#

import requests
import psycopg2
from psycopg2 import pool
import logging
import boto3
import time
from datetime import datetime
import json


sqs = boto3.client('sqs')
# INSERT_CAT = ""
# SELECT_CAT = ""
#
# pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
#                                              user="postgres",
#                                              password="Ihgdp51505150!",
#                                              host="localhost",
#                                              database="Cats")


def ex1():

    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)


def ex2():

    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)

    print(filtered_list)


def ex3():

    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def ex4():

    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))


def ex5():

    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-8')
    print(response)
    while True:
        time.sleep(3)
        msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-8')
        if msg:
            print(msg)
        else:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Polling SQS { now }...")


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

def sort_people(people_list, x, y):
    if y == 'desc':
        people_list.sort(key = lambda p : p[x], reverse=True)
    else:
        people_list.sort(key = lambda p : p[x])

def filter_males(people_list):

    return list(filter(lambda p : p['sex'] == 'male', people_list))

def calc_bmi(people_list):

    list_bmi = list(map(lambda p: {
        'id': p['id'],
        'name': p['name'],
        'weight_kg': p['weight_kg'],
        'height_meters': p['height_meters'],
        'bmi' : round(p['weight_kg'] / p['height_meters'] ** 2, 1)
    },  people_list))
    return list_bmi

def get_people(people_list):

    l15 = [p['name'] for p in people_list if p['age'] >= 15]
    return l15


def send_message_to_sqs(cat, queue_url):

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'UserName': {
                'DataType': 'String',
                'StringValue': cat["cat_name"]
            },
            'UserId': {
                'DataType': 'Number',
                'StringValue': str(cat["cat_id"])
            }
        },
        MessageBody=(
            cat["status"]
        )
    )
    return response['MessageId']


def read_message_from_sqs(queue_url):

    retval = None

    # Read message from SQS queue.
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )

    message = None
    try:
        message = response['Messages'][0]  # Only read one.
    except KeyError as ke:
        logging.info("SQS queue is empty.")

    if message:
        retval = {
            "status": message["Body"],
            "cat_id": message["MessageAttributes"]["UserId"]["StringValue"],
            "cat_name": message["MessageAttributes"]["UserName"]["StringValue"]
        }

        # Delete message once we have read it from the queue.
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )

    return retval

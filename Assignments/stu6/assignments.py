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

sqs = boto3.client('sqs')
INSERT_CAT = "insert into Cats (cat_id, cat_name, status) values (%s, %s, %s)"
SELECT_CAT = "select * from Cats where cat_id $1"

pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                             user="postgres",
                                             password="1141821Gagoka!",
                                             host="localhost",
                                             database="Cats")


def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
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
    filter_males(people_list)
    filtered_list = filter_males(people_list)
    print(filtered_list)


def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    calc_bmi(people_list)
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
        "status": "Feed me human!"
    }
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-6')
    while True:
        time.sleep(2)
        msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-6')
        if msg:
            print(msg)
        else:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Polling SQS { now }...")

def ex6():
    cat = {
        "cat_id": 2,
        "cat_name": "Gypsy",
        "status": "Feed me human, now!"
    }
    save_to_cat_table(cat)
def save_to_cat_table(cat):
    with pg_pool.getconn() as conn:
        with conn.cursor() as cur:
            cur.execute(INSERT_CAT, (cat["cat_id"], cat["cat_name"], cat["status"]))


def ex7():
    print("TODO ...")
    # cat_id = 1
    # cat = get_cat(cat_id)
    # print(cat)

def iga():
    light_list = [
        {"light_id": 1, "voltage": 120, "current": 10},
        {"light_id": 2, "voltage": 110, "current": 20},
        {"light_id": 3, "voltage": 130, "current": 5},
        {"light_id": 4, "voltage": 100, "current": 10},
        {"light_id": 5, "voltage": 110, "current": 10},
    ]
    print(calc_power(light_list))


#
# Place your functions here...
#
def sort_people(people_list, x, y):  #sort w/ lambda
    if y == "asc":
        people_list.sort(key = lambda w: w[x])  #sort by weight in asc order
    else:
        people_list.sort(key = lambda w: w[x], reverse = True)   #sort by weight in desc order


def filter_males(people_list):  #filter
    return list(filter(lambda s: s['sex'] == 'male', people_list))


def calc_bmi(people_list):  #Map
    new_people_list = list(map(lambda b: {
    'id': b['id'],
    'name': b['name'],
    'weight_kg': b['weight_kg'],
    'height_meters': b['height_meters'],
    'bmi': round(float(b['weight_kg']) / b['height_meters'] ** 2, 2)
    }, people_list))
    return new_people_list


def get_people(people_list):
    p = [x['name'] for x in people_list if x['age'] >=15]
    return p


def send_msg(cat, queue_url):
    import boto3
import logging

# sqs = boto3.client('sqs')
# QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/807758713182/siu-queue-1'


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

    #Read message from SQS queue.
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
            "message": message["Body"],
            "user_id": message["MessageAttributes"]["UserId"]["StringValue"],
            "user_name": message["MessageAttributes"]["UserName"]["StringValue"]
        }

        # Delete message once we have read it from the queue.
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )

    return retval




def homework():
    people_list = [
        {'id': 2, 'name': 'bob',     'ssn': '111-11-1111'},
        {'id': 3, 'name': 'charlie', 'ssn': '222-22-2222'},
    ]

    x = list(map(lambda s: {
        'id': s['id'],
        'name': s['name'],
        'ssn': f"xxx-xx-{s['ssn'][7:]}"
    }, people_list))
    print(x)

def calc_power(light_list):
    new_list = list(map(lambda c: {
       'light_id': c['light_id'],
        'watts': c['voltage'] * c['current']
    }, light_list))
    return list(filter(lambda w: w['watts'] > 1000, new_list))

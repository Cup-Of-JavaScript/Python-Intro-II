#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python II
#

# sqs = boto3.client('sqs')
import requests
import psycopg2
from psycopg2 import pool
import logging
import boto3
import time
from datetime import datetime

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-7'
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
    # print("TODO ...")
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
    # print("TODO ...")
    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-7')
    while True:
        time.sleep(3)
        msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-7')
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
# Ex1:
def sort_people(people_list, a, b):
    if b == "asc":
        people_list.sort(key=lambda p: p[a], reverse=False) # Inline Lambda, in-place sort.
    elif b == "desc":
        people_list.sort(key=lambda p: p[a], reverse=True)


# Ex2:
def filter_males(people_list):
    male_only = list(filter(lambda x: x["sex"] == "male", people_list))
    print(male_only)

# Ex3:
def calc_bmi(people_list):
    my_list = list(map(lambda x: {
        "id": x ["id"],
        "weight_kg": x["weight_kg"],
        "name": x["name"],
        "height_meters": x["height_meters"],
        "bmi": (round(float(x["weight_kg"]) / float(x["height_meters"]) ** 2, 1))
    }, people_list))
    return my_list

# Ex4:
def get_people(people_list):
    new_list = [x['name'] for x in people_list if x['age'] != 15]
    return new_list


# Ex5:
def send_message_to_sqs(cat, QUEUE_URL):

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=10,
        MessageAttributes={
            'CatName': {
                'DataType': 'String',
                'StringValue': cat['cat_name']
            },
            'CatId': {
                'DataType': 'Number',
                'StringValue': str(cat['cat_id'])
            }
        },
        MessageBody=(
            cat["status"]
        )
    )
    return response['MessageId']


sqs = boto3.client('sqs')

def read_message_from_sqs(message):
    retval = None
    # Read message from SQS queue.
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
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
            "cat_id": message["MessageAttributes"]["CatId"]["StringValue"],
            "cat_name": message["MessageAttributes"]["CatName"]["StringValue"]
        }

        # Delete message once we have read it from the queue.
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )

    return retval # pg_pool = psycopg2.pool.SimpleConnectionPool
# (1, 20,
# user="postgres",
# password="Ihgdp51505150!",
# host="localhost",
# database="Cats")


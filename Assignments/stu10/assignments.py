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

sqs = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-10'
INSERT_CAT = "insert into cats (cat_id, cat_name, status) values(%s, %s, %s)"
SELECT_CAT = ""

pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                           user="postgres",
                                            password="Floor05$",
                                            host="localhost",
                                            database="Cats")


def ex1():

    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)


def ex2():
    #print("TODO ...")
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_people(people_list)
    print(filtered_list)


def ex3():
    #print("TODO ...")
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def ex4():
    #print("TODO ...")
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
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-10')
    print(response)
    while True:
        time.sleep(3)
        msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-10')
    if msg:
        print(msg)
    else:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Polling SQS { now }...")


def ex6():
    #print("TODO ...")
    cat = {
        "cat_id": 1,
        "cat_name": "Gypsy",
        "status": "hungry"
    }
    save_to_cat_table(cat)


def ex7():
    print("TODO ...")
    cat_id = 1
    # cat = get_cat(cat_id)
    # print(cat)


#
# Place your functions here...
#

#ex1
def sort_people(people_list, x, y):
    if x == 'desc':
        sorted(people_list, key= lambda x: (x["weight"], reversed ==True))
    else:
        sorted(people_list, key= lambda x: x["weight"])

#ex2
def filter_people(people_list):
    return list(filter(lambda x: x["sex"] == "male", people_list))


#ex3
def calc_bmi(people_list):
   new = list(map(lambda i: {
       'id': i['id'],
       'name': i['name'],
       'weight_kg': i['weight_kg'],
       'height_meters': i['height_meters'],
       'bmi': (round(float(i['weight_kg']) / float(i['height_meters']) ** 2, 1))
   }, people_list))
   return new

#ex4
def get_people(people_list):
   l3 = [i['name'] for i in people_list if i['age'] >= 15]
   return l3

#ex5
def send_message_to_sqs(cat, queue_url):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=10,
        MessageAttributes={
            'CatName': {
                'DataType': 'String',
                'StringValue': cat["cat_name"]
            },
            'CatId': {
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

        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )

    return retval

#ex6
def save_to_cat_table(cat):
    with pg_pool.getconn() as conn:
        with conn.cursor() as cur:
            cur.execute(INSERT_CAT, (cat['cat_id'], cat['cat_name'], cat['status']))
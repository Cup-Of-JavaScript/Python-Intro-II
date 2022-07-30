#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#

import requests
import psycopg2
import logging
import boto3
import time
from datetime import datetime

sqs = boto3.client('sqs')

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
    filtered_list = filter_people(people_list)
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
    response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/807758713182/stu-0')
    while True:
        time.sleep(3)
        msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/807758713182/stu-0')
        if msg:
            print(msg)
        else:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Polling SQS { now }...")


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


def filter_people(people):
    return list(filter(lambda p: p['sex'] == 'male', people))


def calc_bmi(people):
    return list(map(lambda p:
                    {
                        'id': p['id'],
                        'name': p['name'],
                        'weight_kg': p['weight_kg'],
                        'height_meters': p['height_meters'],
                        'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1)
                    },
                    people))


def get_people(people):
    return [p['name'] for p in people if p['age'] >= 15]


def send_message_to_sqs(cat, queue_url):
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'CatId': {
                'DataType': 'Number',
                'StringValue': str(cat["cat_id"])
            },
            'CatName': {
                'DataType': 'String',
                'StringValue': cat["cat_name"]
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
            "cat_id": message["MessageAttributes"]["CatId"]["StringValue"],
            "cat_name": message["MessageAttributes"]["CatName"]["StringValue"]
        }

        # Delete message once we have read it from the queue.
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )

    return retval

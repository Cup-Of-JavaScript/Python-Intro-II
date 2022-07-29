#
# File: lec6.py
# Date: 7/4/2022
# Desc: Data access lecture
#

import requests
import psycopg2
import boto3


def lec6():
    # API
    r = requests.get('http://jsonplaceholder.typicode.com/users/1')
    print(r.json())

    # S3
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    # Database
    try:
        con = psycopg2.connect(database='stu0', user='postgres', password='Ihgdp51505150!')
        cur = con.cursor()
        cur.execute('select * from book')
        r = cur.fetchall()  # fetchone()
        print(r)
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    lec6()

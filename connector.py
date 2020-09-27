from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime

import time
import sched
import random


def write_to_database(data):
    cnx = mysql.connector.connect(user='pi', password='password', database='consumption_data')
    cursor = cnx.cursor()

    insert_data = ('INSERT INTO 30s '
            '(geladeira, chuveiro) '
            'VALUES (%s, %s)')

    cursor.execute(insert_data, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def generate_random_data():
    '''This function generates random'''

    data = []
    for i in range(2):
        data.append(random.randint(0, 1000))
    return data


while True:
    data = generate_random_data()
    print(data) 
    write_to_database(data)
    time.sleep(10)














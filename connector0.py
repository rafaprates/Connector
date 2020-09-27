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


    add_data = ('INSERT INTO equipment_kwh '
            '(equipment, kwh) '
            'VALUES (%s, %s)')

    cursor.execute(add_data, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def generate_random_data():
    '''This function generates random data every set interval'''

    # The keys are equipment names and the values are consumption in Kwh
    data = {'geladeira': 0, 'chuveiro': 0,}
    for key in data:
        data[key] = random.randint(0, 1000) 
    #data['agora'] = datetime.now().date()
    return data


# The keys are equipment names and the values are consumption in Kwh
#data = {'geladeira': 0, 'chuveiro': 0}

    #data = generate_random_data()
    #for key, value in data:
    #    data = (key, value, agora) 

while True:
    data = generate_random_data()
    #print(data) 
    for data in data.items(): 
        write_to_database(data)
        print(data)
        print('###')
    time.sleep(10)


#writeToDatabase()




















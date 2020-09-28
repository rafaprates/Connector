from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime

import time
import threading 
import random


def write_to_database(table_name, data):
    cnx = mysql.connector.connect(user='pi', password='password', database='consumption_data')
    cursor = cnx.cursor()

    insert_data = (f'INSERT INTO {table_name} '
            '(geladeira, chuveiro) '
            'VALUES (%s, %s)')

    cursor.execute(insert_data, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def select_from_database():
    cnx = mysql.connector.connect(user='pi', password='password',database='consumption_data')
    cursor = cnx.cursor()

    query = ("SELECT geladeira, chuveiro FROM 30s")
    cursor.execute(query)
    
    # soma as potências 
    total_geladeira = 0
    total_chuveiro = 0
    for (geladeira, chuveiro) in cursor:
        total_geladeira += geladeira
        total_chuveiro += chuveiro

    cursor.close()
    cnx.close()
    return total_geladeira, total_chuveiro

def truncate_table(table_name):
    cnx = mysql.connector.connect(user='pi', password='password',database='consumption_data')
    cursor = cnx.cursor()
    
    cursor.execute(f"TRUNCATE TABLE {table_name}")

    cursor.close()
    cnx.close()


def generate_random_data():
    '''This function generates random'''

    data = []
    for i in range(2):
        data.append(random.randint(0, 1000))
    return data


start = time.time()

#data = select_from_database()
#threading.Timer(60, write_to_database('30min', data)).start()
while True:
    data = generate_random_data()
    print(data) 
    write_to_database('30s', data)
    time.sleep(10)
    
    if (time.time() - start) > 60:
        print("Calculando o somatório do último período...")
        data = select_from_database()
        print("Escrevendo os dados calculados")
        write_to_database('30min', data)
        print("Renovando a Tabela 30s")
        truncate_table('30s')
        start = time.time()
#    end = time.time()
#    elapsed_time = end - start
    #if elapsed time is greater than 30 min
#    if elapsed_time > (1*60):
#        data = select_from_database()    
#        write_to_database('30min', data)





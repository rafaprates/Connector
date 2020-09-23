import time
import sched
import random


def database_connector(equipment, consumption):
    pass

def generate_random_data(data):
    '''This function generates random data every set interval'''

    for key in data:
        data[key] = random.randint(0, 1000) 
    return data






# The keys are equipment names and the values are consumption in Kwh
data = {'geladeira': 0, 'chuveiro': 0}

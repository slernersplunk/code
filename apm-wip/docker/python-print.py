from time import sleep
from random import random, seed
from datetime import datetime

seed(1)

while True:
    y=round(random(),1)+.25
    print('Sleeping: ', y)
    sleep(y)
    print(datetime.now())
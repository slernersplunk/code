from time import sleep
from random import random, seed
x=1
if __name__ == '__main__':
    while x:
        y=round(random(),1)+.25
        print('Sleeping: ', y)
        sleep(y)
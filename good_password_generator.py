import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '*;:.,_-!?/'

all = lower+upper+numbers+symbols
length =  16
password = "".join(random.sample(all, length))
print(password)
print('Please, dont forget to save to not to forget it')
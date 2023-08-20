#Random Password Generator using Python Programming Language
#Author: Burak İrtel

import random
import string

print('This programme generates random password with desired length. Password includes upper case, lower case, number, and characters!. Enjoy')

length = int(input('\nEnter the length of password: '))                      

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)

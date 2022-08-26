'''
112 Warm-up

Questions:
1. What does this code do?
2. What module (like a library) is used and which lines is it used on?
3. What does the variable now contain on line 19?
4. What does the .days0 method do in line 23?
'''

import datetime

#get user birthday
year = int(input('When is your birthday? [YY] '))
month = int(input('When is your birthday? [MM] '))
day = int(input('When is your birthday? [DD] '))
birthday = datetime.datetime(year,month,day)

#calculate days until birthday
now = datetime.datetime.now()
user_birthday = datetime.datetime(now.year, month, day)
difference = user_birthday - now
print(difference.days)
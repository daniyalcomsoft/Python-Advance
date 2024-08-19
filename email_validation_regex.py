#  conditions 
# a-z 
# 0-9
# . _ should be one time
# @ should be one time
# . at the position of 2 or 3

import re
# we are passing range here
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter you Email : ')

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")
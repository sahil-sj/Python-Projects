# a-z sahilmendiratta222@gmail.com
# 0-9
# . _ one time
# @ one time
# . last 3rd and 4th position
# ["h"]\w --\w is used to search any chracter in the string in regex
# / is used before any chracter to search in regex
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" # + is required to merge all the condition, ? means 1 or 0 time
user_email=input("enter your email : ")
if re.search(email_condition,user_email):
    print("Right Email")
else: 
    print("Wrong Email")
# Mini project — age & greeting script
# Input name & age → print greeting with calculated birth year using f-strings.
from datetime import datetime

name = input("enter Your Name : ")
age = int(input("enter Your Age : "))

currentYear = datetime.now().year
birthYear = currentYear - age
print(f"Your Name is {name}")
print(f"Your Age is {age}")
print(f"Your Birth Yaer Is : {birthYear}")
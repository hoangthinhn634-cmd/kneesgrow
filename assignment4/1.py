import re

pattern = r"^[A-Z]{3}[0-9]{3}$"

code = input("Enter course code: ")

if re.match(pattern, code):
    print("Valid")
else:
    print("Invalid")
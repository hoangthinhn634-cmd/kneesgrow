import re

def hide_phone_numbers(text):
    pattern = r"\d{10}|\+84\d+"
    return re.sub(pattern, "[REDACTED]", text)


document = input("Enter document: ")
print(hide_phone_numbers(document))
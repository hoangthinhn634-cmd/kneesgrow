numbers = []

while True:
    user_input = input("gimme numbers (empty = quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))

numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input, please enter a number!")
numbers.sort(reverse=True)

print("Top numbers:")
for num in numbers[:5]:
    print(num)
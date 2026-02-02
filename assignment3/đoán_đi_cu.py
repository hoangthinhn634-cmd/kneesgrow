import random

number = random.randint(1, 10)

while True:
    guess = int(input("đoán từ 1-10 đi cu: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct")
        break
correct_username = "da riel user name"
correct_password = "da riel password"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("welcome")
        break
    else:
        attempts += 1
        print ("Nuh uh! incorrect username or password")

if attempts == 5:
    print("Access denied")

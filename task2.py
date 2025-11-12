#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
user = admin
pass = 12345

correct = True

while correct = True:
    user = str(input("Enter username: "))
    pass = str(input("Enter password: "))
    if user = False or pass = False:
        print("Access denied")
    if user = True and pass = True:
        print("Access granted")
else:
    print("Access denied")
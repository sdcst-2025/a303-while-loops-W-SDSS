##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""

correctuser = "admin"
correctpass = "12345"
maxatt = 3
att = 0

while att < maxatt:
    user = input("Enter username: ")
    pas = input("Enter password: ")
    if user == correctuser and pas == correctpass:
        print("Access granted")
        break
    else:
        print("Access denied")
        att += 1
else:
    print("Too many failed attempts. Access denied.")

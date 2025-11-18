#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
import math

num = ""
incorrectnum = True

while incorrectnum == True:
    num = float(input("Enter number: "))
    even = num%2
    if even != 0:
        print("That is not an even integer")
    if even == 0:
        print("That is an even integer")
    else:
        incorrectnum = False

#even number ni naxtutaatoni tudukukedo odd number no tokini tudukanai
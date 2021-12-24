"""Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. 
Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo". 
The program should behave normally for all other files which exist and don't exist."""

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    EasterEgg = "na na boo boo"
    FName = input("Enter the file's name: ")
    FHandle = open(
        os.path.join(__location__, FName)
    )  # We join the script's directory with a user input!
except:
    if FName == EasterEgg:
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File cannot be opened! Check spelling and try again.")
    exit()

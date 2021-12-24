"""Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case."""

try:
    FHandle = open(input("Enter the file name: "))
except:
    print("File cannot be opened! Check spelling and try again.")
    exit()

for line in FHandle:
    line = line.upper()
    linr = line.rstrip()
    print(line)

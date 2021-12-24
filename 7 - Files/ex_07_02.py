"""Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam confidence values from these lines. 
When you reach the end of the file, print out the average spam confidence."""

# When trying to open a file, it starts looking in the working directory.
# To change this behavior and make it start looking in the script's
# directory, you can use the following OS snippet.

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    FHandle = open(
        os.path.join(__location__, input("Enter the file name: "))
    )  # We join the script's directory with a user input!
except:
    print("File cannot be opened! Check spelling and try again.")
    exit()

TotalConfidence = 0
ConfidenceCounter = 0

for line in FHandle:
    if line.startswith("X-DSPAM-Confidence:"):
        TotalConfidence += float(line[line.find(":") + 1 :])
        ConfidenceCounter += 1

if ConfidenceCounter != 0:
    print(
        "The total Spam Confidence is: {}, the average is: {}.".format(
            TotalConfidence, TotalConfidence / ConfidenceCounter
        )
    )
else:
    print("There were no confidence values in the file!")

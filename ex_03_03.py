from numpy import linspace

while True:
    try:
        studentGrade = float(input("Enter a grade between 0 and 1: "))
        if studentGrade < 0 or studentGrade > 1:
            raise
        break
    except:
        print("\nNot a valid input! Try again.\n")

for counter, value in enumerate(linspace(0.6, 1, 5)):
    if value <= studentGrade:
        continue
    else:
        break

if counter == 0:
    print("Your grade is: {}.".format(chr(70)))
else:
    print("Your grade is: {}.".format(chr(69 - counter)))

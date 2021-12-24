from numpy import linspace


def computeGrade(functionGrade):
    for counter, value in enumerate(linspace(0.6, 1, 5)):
        if value <= functionGrade:
            continue
        else:
            break

    if counter == 0:
        return "Your grade is: F."
    else:
        return "Your grade is: {}.".format(chr(69 - counter))


while True:
    try:
        studentGrade = float(input("Enter a grade between 0 and 1: "))
        if studentGrade < 0 or studentGrade > 1:
            raise
        break
    except:
        print("\nNot a valid input! Try again.\n")

letterGrade = computeGrade(studentGrade)

print(letterGrade)

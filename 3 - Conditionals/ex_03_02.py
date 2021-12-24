while True:
    try:
        timeHour = float(input("Enter your hours worked: "))
        timeRate = float(input("Enter your hourly rate: "))
        break
    except:
        print("\nNot a valid input! Try again.\n")
if timeHour > 40.0:
    timeOvertime = timeHour - 40.0
    print("Your pay is: ${:.2f}.".format(timeRate * (1.5 * timeOvertime + 40.0)))
else:
    print("Your pay is: ${:.2f}.".format(timeHour * timeRate))

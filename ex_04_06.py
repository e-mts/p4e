def computePay(functionHour, functionRate):
    if functionHour > 40.0:
        timeOvertime = functionHour - 40.0
        return "Your pay is: ${:.2f}.".format(
            functionRate * (1.5 * timeOvertime + 40.0)
        )
    else:
        return "Your pay is: ${:.2f}.".format(functionHour * functionRate)


while True:
    try:
        timeHour = float(input("Enter your hours worked: "))
        timeRate = float(input("Enter your hourly rate: "))
        break
    except:
        print("\nNot a valid input! Try again.\n")

print(computePay(timeHour, timeRate))

fTemp = False
while fTemp == False:
    fTemp = input("Enter the temperature in °F: ")
    try:
        fTemp = float(fTemp)
    except:
        fTemp = False
        print('Not a number! Try again.\n')
print('{}°F = {:.2f}°C.'.format(fTemp, (fTemp - 32.0) * 5.0 / 9.0))

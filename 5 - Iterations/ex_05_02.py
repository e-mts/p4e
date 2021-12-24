count = False
smallest_number = None
largest_number = None

while True:
    try:
        current_value = input("Enter a number: ")
        current_value = float(current_value)
    except:
        if current_value == "done" or current_value == "Done":
            break
        else:
            print("\nNot a valid entry! Try again.\n")
            continue

    if smallest_number is None or current_value < smallest_number:
        smallest_number = current_value

    if largest_number is None or largest_number < current_value:
        largest_number = current_value

    count = True

if count is False:
    print("There were no inputs!")
else:
    print("Max Value: {}, Min Value: {}.".format(largest_number, smallest_number))

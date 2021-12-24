count = 0
total_sum = 0

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

    total_sum += total_sum + current_value
    count += 1

if count == 0:
    print("There were no inputs!")
else:
    print(
        "Total sum: {}, Number of entries: {}, Average: {}.".format(
            total_sum, count, (count / total_sum) ** -1
        )
    )

stored_numbers = []
while True:
    number = input("Enter a number : ")
    try:
        if number.lower() == "done":
            print(f"Maximum : {max(stored_numbers)}")
            print(f"Minimum : {min(stored_numbers)}")
            break
        number = int(number)
    except:
        print("\tInvalid Input")
        continue
    number = float(number)
    stored_numbers.append(number)
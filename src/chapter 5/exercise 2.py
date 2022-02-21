numbers = []
while True:
    num = input("Enter number: ")
    try:
        num = int(num)
        numbers.append(num)
    except:
        if num.lower() == 'done':
            break
        else:
            print("Invalid input")
            continue

print(max(numbers),min(numbers))
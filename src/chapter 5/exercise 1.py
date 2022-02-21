total = 0

count = 0

numbers = []

while True:
    num = input('Enter number; ')

    try:
        num = int(num)
        numbers.append(num)
        count = count + 1
    except:
        if num.lower() == "done":
            break
        else:
            print('Invalid input')

total = total + sum(numbers)
print("Average: ", total/count)
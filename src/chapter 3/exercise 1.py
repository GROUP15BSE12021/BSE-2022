hours = float(input('Enter hours: '))

rate = float(input('Enter rate: '))

if hours <= 40:
    pay = hours * rate
    print('Your pay is:  ', pay)

else:
    extra_hours = hours - 40
    pay = 40 * rate + extra_hours * 1.5
    print('Your pay is:  ', pay)

guests = input('Enter number of guests:  ')

try:
    guests = int(guests)
    if guests <= 50:
        print('Price is $4000')
    elif guests <= 100:
        print('Price is $10000')
    elif guests <= 200:
        print('Price is $15000')
    else:
        print('Price is $20000')

except:
    print('Enter an integer')
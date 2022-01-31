amount=float(input('Enter the amount to make change for '))
print('your change is ')
if amount>20:
    change=amount//20
    print(change,'twenties')
    remainder1=amount%20
if remainder1>10:
    change=remainder1//10
    print(change,'tens')
    remainder2=remainder1%10
if remainder2>5:
    change=remainder2//5
    print(change,'fives')
    remainder3=remainder2%5
if remainder3>1:
    change=remainder3//1
    print(change,'ones')
    remainder4=remainder3%1
if remainder4>0.25:
    change=remainder4//0.25
    print(change,'quarters')
    remainder5=remainder4%0.25
if remainder5>0.1:
    change=remainder5//0.1
    print(change,'dimes')
    remainder6=remainder5%0.1

if remainder6>0.05:
    change=int(remainder6//0.05)
    print(change,'nickels')
else:
    change=remainder6//0.01
    print(change,'pennies')


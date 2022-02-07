age = input('Enter your age please : ')

try :
    age = int(age)
    if age >= 18:
        print('You can vote')
    elif 0 <= age <= 17:
        print('Too young to vote')
    else :
        print('You are a time traveller')

except:
    print('Error, please enter integer')

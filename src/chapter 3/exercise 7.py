location_input = input('Enter location :  ').lower()

pay_input = int(input('Enter pay : '))

if location_input == 'mbarara':
    if pay_input > 4000000:
        print('I will work ')
    else :
        print('No thanks i can find something better')

elif location_input == 'kampala':
    if pay_input >= 10000000:
        print('I will work')
    else:
        print('No way!')

elif location_input == 'space':
    print('Without a doubt i will work ')

else:
    if  pay_input >= 6000000:
        print('Sure i will take the job')
    else:
        print('No thanks, i will get something better')


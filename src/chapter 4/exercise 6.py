def compute_pay():
    try:
        hours = float(input('Enter hours: '))

        rate = float(input('Enter rate: '))

        if hours <= 40:
            pay = hours * rate


        else:
            extra_hours = hours - 40
            pay = 40 * rate + extra_hours * 1.5
        return pay
    except ValueError:
        print('Error, please enter numeric input!')


print('your pay is: ', compute_pay())

c = float(input("enter initial amount "))
r = float(input('enter  yearly rate '))
t = int(input("number of years till maturation "))
n = float(input("number of times interest is compounded per year "))


def investiments(c,r,t,n):
    I = c * r * t
    p = c * (I + (t / n)) ** (t*n)
    return round(p,2)


print('final value of investment is ',investiments(c,r,t,n))
c=float(input("enter initial amount "))
r=float(input('enter  yearly rate '))
t=int(input("number of years till maturation "))
n=float(input("number of times interest is compounded per year "))
I=c*r*t
p=c*(I+(t/n))**r
print('final value of investment is ',round(p,2))
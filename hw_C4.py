from math import sqrt
def quadratic_equation(a, b, c):
  D=b^2-4*a*c
  if D<0:
    print('Корней нет. P.s: они есть, но по условию просят так написать')
  elif D>=0:
    print((-b+sqrt(D))/(2*a), (-b-sqrt(D))/(2*a))

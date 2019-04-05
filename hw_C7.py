from math import sin
import numpy as np

def integer(a, b, N):
  f=sin
  k=float(b-a)/N
  c=sum([f(x) for x in range(0, N)])*k
  return c
#вывести integer()

import random
m=random.randint(1,100)
while n!=m:
    n=int(input("Угадай число от 1 до 100 "))
    if n>m:
      print("Меньше")
    elif n<m:
      print("Больше")
    else:
      print(("Вы угадали") + str(m))

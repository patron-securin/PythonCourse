def encoding(n):
    if n == 1:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
    return True
def prime_number(n = 1):
    while True:
        if encoding(n): 
            yield n
        n += 1
for n in prime_number():
    if n > 10000: 
        break
    print(n)

import time
start = time.time()
a, b = 1 , 2
result = 0
while a and b < 4_000_000:
    a , b = b, a + b
    if a % 2 == 0:
        result += a
print(result)
print(time.time() - start)

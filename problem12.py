import time
import math
start = time.time()


def triang(n):
    result = 1
    for i in range(2, n + 1):
        result += i
    return result


n = 1
count = 0
while True:
    n += 1
    result = triang(n)
    for i in range(1, int(math.sqrt(result)) + 1):
        if result % i == 0:
            count += 2
    if count > 500:
        break
    count = 0


print("Result = ", result)
print("elapsed time :", time.time() - start)

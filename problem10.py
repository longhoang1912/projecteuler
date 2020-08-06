from prime import is_prime
import time
start = time.time()


def primebelow(number):
    result = 0
    for i in range(2, number):
        if is_prime(i):
            result += i
    return result


print("result = ", primebelow(2_000_000))
print("elapsed time", time.time() - start)

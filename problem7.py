from prime import is_prime
import time
start = time.time()


def th(n):
    result = 1
    count = 0
    while count < n:
        result += 1
        if is_prime(result):
            count += 1

    return result


print("Result = ", th(10001))
print("elapsed time:", time.time() - start)

import time
import math
start = time.time()


def is_prime(n):
    prime = True
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return prime


def langest_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i) and n % i == 0:
            result = i
    return result


def main():

    print("result = ", langest_prime(600851475143))
    print("elapsed time:", time.time() - start)


if __name__ == "__main__":
    main()

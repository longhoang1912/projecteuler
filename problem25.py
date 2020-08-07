import time
start = time.time()


def index1000fibo():
    a, b = 1, 2
    count = 2
    while True:
        a , b = b, a + b
        count += 1
        if len(str(a)) == 1000:
            break
    return count


def main():
    print("result =", index1000fibo())
    print("elapsed time:", time.time() - start)


if __name__ == "__main__":
    main()

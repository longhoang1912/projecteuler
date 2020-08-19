import time
start = time.time()
def coolatz(n):
    result = n
    count = 1
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
        if n == 1:
            break
    return count, result


result = max([coolatz(i) for i in range(500_000, 1_000_000)])
print(result)
print("time: ", time.time() - start)
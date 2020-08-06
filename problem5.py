import time
start = time.time()


def isdivison(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


result = 1
while True:
    if isdivison(result):
        break
    result += 1
print(result)
print(time.time() - start)

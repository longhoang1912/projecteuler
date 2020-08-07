import time
start = time.time()
result = 0
for i in range(1, 1001):
    result += i ** i
print("Result = ",str(result)[-10:])
print("elapsed time: ", time.time() - start)
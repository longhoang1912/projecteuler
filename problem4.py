import time
start = time.time()
result = max([i * j for i in range(1000, 99, -1)
              for j in range(1000, 99, -1) if str(i * j) == str(i * j)[::-1]])
print("result = ", result)
print("Elapsed time : ", time.time() - start)

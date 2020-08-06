import time
start = time.time()
result = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
print(result)
print(time.time() - start)

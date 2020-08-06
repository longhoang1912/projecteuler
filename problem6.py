import time
start = time.time()
sumofsqua = sum([i**2 for i in range(1, 101)])
squaofsum = sum([i for i in range(1, 101)])**2
result = squaofsum - sumofsqua
print("result = ", result)
print("elapsed time : ", time.time() - start)

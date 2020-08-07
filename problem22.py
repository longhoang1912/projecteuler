import time
start = time.time()
with open('p022_names.txt') as f:
    s = f.read()
data = s.lower().replace('"', "").split(",")
data = sorted(data)
point = 0
result = 0
for name in data:
    for char in name:
        point += (ord(char) - 96)
    result += point * (data.index(name) + 1)
    point = 0
print("result=", result)
print("elapsed time:", time.time() - start)

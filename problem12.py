result = 1
a = []
count = 0
while True:
    count = 0
    result += 1
    for i in range(1, result + 1):
        if result % i == 0:
            count += 1
    if count == 4:
        a.append(result)
print(a)

def is_factorials(n):
    result = 0
    for i in str(n):
        temp = 1
        for j in range(1, int(i) + 1):
            temp *= j
        result += temp
    if result == n:
        return True
    else:
        return False


result = 0
count = 3
while count < 2_000_000:
    if is_factorials(count):
        result += count
        count += 1
    else:
        count += 1
print(result)

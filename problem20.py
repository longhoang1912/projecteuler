def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


result = 0
for i in str(factorial(100)):
    result += int(i)
print(result)

import time
start = time.time()


def pitago():
    for a in range(800, 50, -1):
        for b in range(800, 50, -1):
            for c in range(1000, 100, -1):
                if a + b + c == 1000 and a**2 + b ** 2 == c ** 2:
                    return (a * b * c)


print(pitago())
print(time.time() - start)

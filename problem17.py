

def text_number(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 <= n <= 99 and n % 10 != 0:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000 and n % 100 == 0:
        return ones[n // 100] + "hundred"
    elif 100 < n < 1000 and n % 100 != 0:
        return ones[n // 100] + "hundredand" + text_number(n % 100)
    # elif 100 < n < 1000 and n % 100 != 0:
    #     if n % 100 == 10:
    #         return ones[n // 100] + "hundredten"
    #     elif 0 < n // 10 < 20:
    #         return ones[n // 100] + "hundred" + ones[n % 100]
    #     elif 2 <= n // 10 % 10 <= 9:
    #         return ones[n // 100] + "hundred" + tens[n // 10 % 10]
    #     else:
    #         return ones[n // 100] + "hundred" + tens[n // 10 % 10] + ones[n // 100]
    elif n == 1000:
        return "onethousand"
        # elif :
        #     return
    # elif 120 < n < 1000 and n % 10 == 0:
    #     return ones[n // 100] + "hundred" +
    # elif 100 < n < 1000 and n % 100 != 0:
    #     return ones[n // 100] + "hundred and " + tens[n / 10] + ones[n % 10]


def count(n):
    result = 0
    for i in range(1, n + 1):
        result += len(text_number(i))
    return result

def main():
    print(count(1000))


if __name__ == "__main__":
    main()

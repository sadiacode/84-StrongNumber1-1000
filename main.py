num = 1
while num <= 1000:
    original = num
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        i = 1
        factorial = 1
        while i <= digit:
            factorial *= i
            i += 1
        sum += factorial
        temp //= 10
    if original == sum:
        print(original)
    num += 1
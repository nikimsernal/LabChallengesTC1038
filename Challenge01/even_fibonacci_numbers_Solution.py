def sum_even_fibo(limit):
    a, b = 1, 2
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum


print(sum_even_fibo(4000000))  # Output: 4613732

def sum_even_fibs_until_n(n):
    res = 0
    a, b = 1, 2

    while a <= n:
        if a % 2 == 0:
            res += a
            
        a, b = b, a + b

    return res

print(sum_even_fibs_until_n(4000000))



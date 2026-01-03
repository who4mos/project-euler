def sum_odd_squares(n):
    res = 0
    for i in range(1, n+1, 2):
        res += i * i

    return res

print(sum_odd_squares(536000))

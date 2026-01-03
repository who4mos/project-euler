def is_3_or_5_mult(n):
    if n % 3 == 0 or n % 5 == 0:
        return True

    return False

def sum_of_3_or_5_mults_below_n(n):
    res = 0
    for i in range(1, n):
        if is_3_or_5_mult(i):
            res += i

    return res

print(sum_of_3_or_5_mults_below_n(1000))

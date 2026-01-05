def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def prime_sum_below_n(n):
    res = 0
    i = 2
    
    while i < n:
        if is_prime(i):
            res += i

        i += 1

    return res

print(prime_sum_below_n(2000000))

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def find_nst_prime(n):
    i = 2
    count = 0
    
    while True:
        if is_prime(i):
            count += 1

        if count == n:
            return i

        i += 1


print(find_nst_prime(10001))
    

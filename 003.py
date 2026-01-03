def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def factors(n):
    sqrt_n = n ** 0.5
    fs = []
    
    for i in range(2, int(sqrt_n)+1):
        if n % i == 0:
            if is_prime(i):
                fs.append(i)

    return sorted(fs)[-1]

print(factors(600851475143))



        

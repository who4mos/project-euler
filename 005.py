def smallest_evenly_divisible_by(start, stop):
    n = start
    if n % 2 != 0:
        n += 1

    while True:
        for i in range(start, stop + 1):
            if n % i != 0:
                break
        else:
            return n

        n += 2
            

print(smallest_evenly_divisible_by(1, 20))

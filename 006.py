def sum_of_squares_first_n_naturals(n):
    res = 0
    for i in range(1, n+1):
        res += i ** 2

    return res

def square_of_sum_first_n_naturals(n):
    res = 0
    for i in range(1, n+1):
        res += i

    return res ** 2

print(square_of_sum_first_n_naturals(100)
      - sum_of_squares_first_n_naturals(100))
        

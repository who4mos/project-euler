def is_palindrome(n):
    n_string = str(n)
    for i in range(len(n_string) // 2):
        if n_string[i] != n_string[-1 - i]:
            return False

    return True

def palindromes_product_of_n_digits(n):
    start = int("9" * n)
    end = int("1" + "0" * (n - 1))
    ps = []
    
    for i in range(start, end - 1, -1):
        for j in range(i, end - 1, -1):
            p = i * j
            if is_palindrome(p):
                ps.append(p)

    return ps


print(max(palindromes_product_of_n_digits(3)))
    

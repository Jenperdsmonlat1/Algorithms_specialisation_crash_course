
numbers = open("numbers.txt", "r").read().split()
int_numbers = [int(x) for x in numbers]



def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y
    
    m = max(len(str(x)), len(str(y))) // 2
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba(a + b, c + d)
    
    return p1 * 10**(2*m) + (p3 - p1 - p2) * 10**m + p2


print(karatsuba(int_numbers[0], int_numbers[1]))

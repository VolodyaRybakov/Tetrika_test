def get_dividers_n(num, k):
    retval = 0
    while num % k == 0 and num:
        num /= k
        retval += 1
    return retval


def get_zeros(n):
    n_2 = 0
    n_5 = 0
    for val in range(n+1):
        n_2 += get_dividers_n(val, 2)
        n_5 += get_dividers_n(val, 5)
    return n_2 if n_2 < n_5 else n_5


print(get_zeros(50000))

import math


def get_zeros(n):
    fact = math.factorial(n)
    result = 0
    while fact % 10 == 0:
        result += 1
        fact //= 10
    return result


try:
    print(get_zeros(50000))
except OverflowError:
    print("Error! Number is too big.")

# Сложность алгоритма O(n)

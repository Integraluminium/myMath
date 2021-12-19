from myMathModule.tools.basic import factorial


def ncr(n: int, k: int) -> int:  # n Choose r   -> math.comb
    n = abs(int(n))
    k = abs(int(k))
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


def npr(n):
    n = abs(int(n))
    k = abs(int(k))
    return int(factorial(n) / factorial(k))


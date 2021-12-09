def my_round(number: float, digits: int = 2) -> float:
    return (int((number*10**digits)+0.5))/10**digits


def prod(*iterable, start=1):
    res = start
    for i in iterable:
        res *= int(i)
    return res


def factorial(num: int) -> int:
    num = int(num)
    if num < 0:
        raise ValueError(f"num > 0 and element of int, {num}")
    counter = 1
    res = 1
    while counter <= num:
        res *= counter
        counter += 1
    return res


if __name__ == '__main__':
    print(my_round(74863.5649, 2))
    print(prod(*(2, 3, 4), start=9))
    print(factorial(5))

import sys


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


def myround(num: float, digits: int) -> float:
    return (int((num*10**digits)+0.5))/num*10**digits


def ncr(n: int, k: int) -> int:  # n Choose r
    n = abs(int(n))
    k = abs(int(k))
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


def binominal(n: int, p: float):
    n = abs(int(n))
    if not 0 <= p <= 1:
        raise ValueError(f"0 <= p <= 1, {p=}")

    def binominal_function(X: int) -> float:
        if X > n:
            return float("NaN")
        return ncr(n, X) * p**X * (1-p)**(n-X)

    return binominal_function

def pri(func):
    def wrapper(*arg):
        _, *q = arg
        print(f"P({q[0]}<=X<={q[1]})", "=", round(func(*arg), 4))
    return wrapper


def get_binominal(binominal, x):
    if type(x) == int:
        print(x, round(binominal(x), 3))
    elif hasattr(binominal, '__iter__'):
        print(sum(binominal(x) for x in binominal))


def get_n(p: float, upper: int, soll: float):
    n = 10
    old = float("nan")
    while True:
        a = binominal(n, p)
        if (new := sum(a(x) for x in range(0, upper+1))) < soll:
            print(f"{n=} -> {new=}")
            n -= 1
            old = new
        elif new >= soll > old:
            print(f"Answ: {n=} hat die Wahrscheinlichkeit {round(new, 4)}")
            return n
        else:
            print(f"{n=} ++> {round(new, 4)=}")
            n += 10

def get_n2(p: float, lower: int, soll: float):
    n = 10
    old = float("nan")
    while True:
        a = binominal(n, p)
        if (new := sum(a(x) for x in range(lower, n+1))) < soll:
            print(f"{n=} -> {new=}")
            n += 1
            old = new
        elif new >= soll > old:
            print(f"Answ: {n=} hat die Wahrscheinlichkeit {round(new, 4)}")
            return n
        else:
            print(f"{n=} ++> {round(new, 4)=}")
            n -= 10

def get_k(n: int , p: float, soll: float):
    k = 0
    bino = binominal(n, p)
    while True:
        out = sum(bino(x) for x in range(k, n+1))
        if out > soll:
            print(f"{k=} -> {round(out, 4)=}")
            k += 1
        elif out <= soll:
            print(f"Answ: {k=} hat die Wahrscheinlichkeit {round(out, 4)}")
            return k


@pri
def get_binominal_range(binominal, min, max):
    return sum(binominal(x) for x in range(min, max+1))

def console_main():
    n = int(input("n >"))
    p = float(input("p >"))
    func = binominal(n, p)
    print("*"*50, "\n")

    while True:
        raw = input("lower, upper >").lower()
        if raw in ("stop", "exit", "quit", ""):
            sys.exit()

        raw = raw.replace(",", " ")
        out = raw.split(" ")
        if len(out) > 1:
            lower, upper, *_ = out
            try:
                lower = int(lower)
                upper = int(upper)
            except TypeError as e:
                raise TypeError(e)

            finally:
                get_binominal_range(func, lower, upper)
        elif len(out) == 1:
            try:
                x = int(out[0])
            except:
                TypeError()
                continue
            else:
                print(func(x))


if __name__ == '__main__':
    console_main()

    # get_n(0.25, 0, 0.05)
    get_n2(0.16666, 1, 0.95)
    # get_k(15, 0.2, 0.1)

    # n = 100
    # p = 0.05
    #
    # a = binominal(n, p)
    # # get_binominal(a, 3)
    # # get_binominal(a, range(0, 1))
    # # get_binominal_range(a, 0, 2)
    # # get_binominal_range(a, 3, n)
    # # get_binominal_range(a, 4, 7)
    # # get_binominal_range(a, 5, 5)
    # # get_binominal_range(a, 0, 0)
    # get_binominal_range(binominal(100, 0.05), 4, 8)
    #
    #
    # # for i in range(0, 10):
    # #     print(i, factorial(i))

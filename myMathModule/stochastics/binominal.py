import math

from combination import ncr


# def binominal(n: int, p: float):
#     n = abs(int(n))
#     if not 0 <= p <= 1:
#         raise ValueError(f"0 <= p <= 1, {p=}")
#
#     def binominal_function(X: int) -> float:
#         if X > n:
#             return float("NaN")
#         return ncr(n, X) * p**X * (1-p)**(n-X)
#
#     return binominal_function


class Binominal:
    def __init__(self, n: int, p: float):
        if not 0 <= p <= 1:
            raise ValueError(f"0 <= p <= 1, {p=}")
        self.n = abs(int(n))
        self.p = float(p)
        self.mean = self.n * self.p
        self.varianz = self.mean * (1-self.p)
        self.deviation = math.sqrt(self.n * self.p * (1-self.p))

    def binompdf(self, k: int) -> float:     # binomial probability density function
        if (k := abs(int(k))) > self.n:
            raise ValueError("k cannot be bigger than n!")
        return ncr(self.n, k) * self.p**k * (1-self.p)**(self.n-k)

    def binomcdf(self, lower_border: int, upper_border: int) -> float:
        if upper_border == "n":
            upper_border = self.n
        lower_border = int(lower_border)
        upper_border = int(upper_border)
        return sum(self.binompdf(x) for x in range(lower_border, upper_border+1))

    def get_all(self):
        return {k: self.binompdf(k) for k in range(self.n)}

    def get_mean(self) -> float:     # Erwartungswert
        return self.n * self.p

    def get_varianz(self) -> float:
        return self.n * self.p * (1-self.p)

    def get_deviation(self) -> float:    # Standardabweichung
        return math.sqrt(self.n * self.p * (1-self.p))

    def get_sigma_distribution(self, z: float= 1) -> float:
        lower = self.mean - z*self.deviation
        upper = self.mean + z*self.deviation
        if int(lower) < lower:
            lower = int(lower) + 1
        if int(upper) < upper:
            upper = int(upper) - 1
        return self.binomcdf(lower, upper)

    def __str__(self) -> str:
        return f"B(k| {self.p}, {self.n})"

    def __eq__(self, other) -> bool:
        return self.n == other.n and self.p == other.p

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __call__(self, *k_params):
        if len(k_params) == 1:
            return self.binompdf(k_params[0])
        return tuple([self.binompdf(k) for k in k_params])


class SimpleBinominal(Binominal):
    def __init__(self, n: int, p: float):
        super(SimpleBinominal, self).__init__(n, p)

    def sim_binompdf(self, k: int) -> float:
        res = super(SimpleBinominal, self).binompdf(k)
        res = round(res, 4)
        print(f"B({k}| {self.p}, {self.n}) = {res} =~ {round(res*100, 2)}%")
        return res

    def sim_binomcdf(self, lower_border: int, upper_border: int) -> float:
        res = super(SimpleBinominal, self).binomcdf(lower_border, upper_border)
        res = round(res, 4)
        print(f"P({lower_border}<=X<={upper_border}) = {res} =~ {round(res*100, 2)}%")
        return res

    def sim_get_sigma_distribution(self, z: float = 1) -> float:
        res = round(super(SimpleBinominal, self).get_sigma_distribution(z), 4)
        print(f"{str(func)} = {round(res*100, 2)}%")
        return res


if __name__ == '__main__':
    func = Binominal(1000, 0.5)
    print(func.get_all())
    print(func(5))
    # # func2 = Binominal(100, 0.5)
    # # func3 = Binominal(101, 0.5)
    # print(func.binompdf(50))
    # # print(my_round(func.binompdf(40), 8))
    # #
    # # print(func.binomcdf(0, 100))
    # #
    # # print(func == func2)
    # # print(func == func3)
    # #
    # # print(func)
    # #
    # # print(func3.deviation)
    # # print(func3.mean)
    # # print(func(2, 3))
    # print(func.binompdf(50))
    # print(func.binomcdf(35, 65))
    # print(func.get_sigma_distribution())
    # print(func.get_sigma_distribution(3))
    for n in range(1000, 10000, 2):
        func = SimpleBinominal(n, 0.5)
        # print(func.binompdf(50))
        # print(f"{str(func)} = {round(func.get_sigma_distribution(1.96)*100, 2)}%")
        func.sim_get_sigma_distribution(3)


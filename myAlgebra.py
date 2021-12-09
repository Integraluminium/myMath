def _make_polynompairs(g, h, fillvalue=None):  # g und h sind Polynomfunktionen
    i = 1                                      # Verbindet gleichwertige Koeffizienten von zwei Funktionen als Tuple
    output_list = []
    g = g.coeffs
    h = h.coeffs
    while (i < len(g) + 1) or (i < len(h) + 1):
        #   print(output_list)
        if len(g) + 1 <= i < len(h) + 1:
            output_list.append((fillvalue, h[-i]))
        elif len(h) + 1 <= i < len(g) + 1:
            output_list.append((g[-i], fillvalue))
        else:
            output_list.append((g[-i], h[-i]))
        i += 1
    return list(output_list[::-1])

# def round(value: float, decimals: int) -> float:
#     return (value*decimals)

class Polynom:
    def __init__(self, *coefficients):
        self.coeffs = list(coefficients)
        self.DEGREE = len(self.coeffs) - 1

    def __str__(self):  # 3x^3+2x-5
        def get_summand_str(coeff, power):
            if abs(coeff) == 0:
                return ""
            if power not in (0, 1):
                if coeff == 1:
                    return f" +x^{power}"
                elif coeff < 1:
                    return f" {coeff}*x^{power}"
                elif coeff > 1:
                    return f" +{coeff}*x^{power}"
                else:
                    return " ERROR "
            elif power == 0:
                if coeff > 1:
                    return f" +{coeff}"
                else:
                    return f" {coeff}"
            elif power == 1:
                if coeff > 1:
                    return f" +{coeff}+x"
                else:
                    return f" {coeff}+x"

        arg_string = ""
        if len(self.coeffs) == 1:
            if self.coeffs[0] == 0:
                return "0"
        if len(self.coeffs) <= 0:
            return "0"
        for i in range(self.DEGREE + 1):
            power = self.DEGREE - i
            coeff = self.coeffs[i]
            arg_string += get_summand_str(coeff, power)
        arg_string = arg_string[2:]
        return arg_string

    def __add__(self, other):   # Lässt Polynome addieren
        zipped_coefficients = _make_polynompairs(self, other, 0)
        new_coefficients = (a + b for a, b in zipped_coefficients)
        return Polynom(*new_coefficients)

    def __sub__(self, other):   # Lässt Polynome subtrahieren
        zipped_coefficients = _make_polynompairs(self, other, 0)
        new_coefficients = (a - b for a, b in zipped_coefficients)
        return Polynom(*new_coefficients)

    def __eq__(self, other):    # Lässt Polynome miteinander Vergleichen
        if self.coeffs == other.coeffs:
            return True

    def get_string(self, name: str):
        """Gibt den Funktionswert als Gleichung aus"""
        return f"{name}(x) = {self.__str__()}"

    def __call__(self, x):
        """Gibt den Funktionswert zurück"""
        # print(list(enumerate(self.coeffs[::-1])))
        return sum(a * x ** i for i, a in enumerate(self.coeffs[::-1]))

    def integrate(self, a: float, b: float):
        antiderivative = self.antiderivate(0)
        return antiderivative.__call__(b) - antiderivative.__call__(a)

    def solve(self, decimals=10, start=0):    # x^3 -0.5+x +2 = 0
        """Solves the Polynom with Newton Algorithm, WARNING: there can be more or less than one solution"""  #TODO equation
        if self.DEGREE < 1:  # Gerade: f(x) = c
            return None
        x, i = start, 0
        xn = start+1
        while round(x, decimals) != round(xn, decimals) and i <= 50:    # Schleife läuft solange, bis sich die Werte
            i += 1                                                      # asymptotisch nähern, oder Schleifenabbruch
            xn = x
            if self.get_slope(xn) == 0:     # NOTFALL KORREGIERUNG, damit nicht durch null geteilt wird
                print("Wurde Korrigiert")
                x += 1
                continue
            x = self.newton_algorithm(xn)

        if round(self(x)) == 0:
            return x
        return None

    def get_slope(self, x: float, x2=None):
        """Slope"""
        if not x2:
            h = 0.0001
            return (self(x+h)-self(x))/h    # lim(f(x)) für h -> 0
        else:
            """average rate of change"""
            if x >= x2:
                raise ValueError("X2 <= x, x2 has to be greater")
            if type(x2) not in (int, float):
                raise TypeError("X2 is not of type int or float")
            return (self(x2)-self(x))/(x2-x)


    def newton_algorithm(self, x):
        return x - self(x) / self.get_slope(x)

    def derivate(self):
        """Gibt Ableitung zurück"""
        derivated = []
        enumerated = list(list(enumerate(self.coeffs[::-1]))[:0:-1])    # nummeriert die Koeffizienten mit den Potenzen
        # print(enumerated)                                             # durch, sortiert wieder zurück in Reihenfolge
        for power, coeff in enumerated:
            # print(power, coeff)
            derivated.append(power*coeff)
        return Polynom(*derivated)

    def antiderivate(self, c=0):
        """Gibt Stammfunktion zurück"""
        if type(c) != int:
            raise TypeError("parameter is not type int")
        integrated = []
        moved_coeff = self.coeffs.copy()
        moved_coeff.append(1)
        enumerated = list(list(enumerate(moved_coeff[::-1]))[::-1])
        for power, coeff in enumerated[:-1]:
            integrated.append(coeff/power)
        integrated.append(c)
        return Polynom(*integrated)





if __name__ == '__main__':
    f = Polynom(1, 0, -0.5, 2)
    g = Polynom(5 / 2, 2, 4)
    f = Polynom(1,0, -1)
    # f = Polynom(1, -1.5, 1, -1.5)
    # print(f"f(x) = {f}")
    print(f.get_string("f"))
    # for x in range(-3, 4, 1):
    #     print(f"f({x}) = {f(x)} {f.get_slope(x)}")
    # print(f.derivate())
    # print(f.integrate(-1, 1))
    print(f.solve(start=0))
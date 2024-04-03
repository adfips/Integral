import itertools
from collections.abc import Iterable


class Polynom:
    def __init__(self, *polynom):
        if len(polynom) == 1:
            seq = polynom[0]
            if isinstance(seq, Polynom):
                self.polynom = seq.polynom[:]
            elif isinstance(seq, Iterable):
                self.polynom = list(seq)
        else:
            self.polynom = [i + 0 for i in polynom]
        self.multipliers = []

    def __getitem__(self, index):
        return self.polynom[index]

    def __setitem__(self, key, value):
        self.polynom[key] = value

    def __eq__(self, val):
        "Test self==val"
        if isinstance(val, Polynom):
            return self.polynom == val.polynom
        else:
            return len(self.polynom) == 1 and self.polynom[0] == val

    def __str__(self):
        res = []
        for index, coef in enumerate(self.polynom):
            if coef != 0:
                if index == 0:
                    index = ''
                elif index == 1:
                    index = 'X'
                else:
                    index = 'X^' + str(index)
                res.append(str(coef) + index)
        if res:
            res.reverse()
            return ' + '.join(res)
        else:
            return "0"

    def __len__(self):
        return len(self.polynom)

    def __add__(self, polynomial):
        if not isinstance(polynomial, Polynom):
            return
        res = [a + b for a, b in itertools.zip_longest(self.polynom, polynomial.polynom, fillvalue=0)]
        return self.__class__(res)

    def __sub__(self, val):
        return self.__add__(-val)

    def __neg__(self):
        return self.__class__([-co for co in self.polynom])

    def __mul__(self, polynomial):
        if not isinstance(polynomial, Polynom):
            return
        poly1 = polynomial.polynom
        poly2 = self.polynom
        res = [0] * (len(poly1) + len(poly2) - 1)
        for index1, value1 in enumerate(poly1):
            for index2, value2 in enumerate(poly2):
                if value1 != 0 and value2 != 0:
                    res[index1 + index2] += value1 * value2
        return self.__class__(res)

    def __pow__(self, degree):
        multiplier = Polynom(self[:])
        res = multiplier
        if isinstance(degree, int):
            for i in range(degree - 1):
                res *= multiplier
        return self.__class__(res)

    def __truediv__(self, divisor):
        """
        Деление многочленов
        :return целая часть, остаток
        """
        if not isinstance(divisor, Polynom):
            return None
        quotient = Polynom([0] * len(self))
        remainder = self
        while len(remainder) >= len(divisor):
            div_degree = len(remainder) - len(divisor)
            div_coef = remainder.polynom[-1] / divisor.polynom[-1]
            quotient[div_degree] = div_coef
            monomial = Polynom([0] * (div_degree + 1))
            monomial[-1] = div_coef
            remainder = remainder - divisor * monomial
            remainder.trim()
        quotient.trim()
        return quotient, remainder

    def trim(self):
        """
        убирает страшие нулевые коэффициенты
        """
        polynom = self.polynom
        if polynom:
            offset = len(polynom) - 1
            if polynom[offset] == 0:
                offset -= 1
                while offset >= 0 and polynom[offset] == 0:
                    offset -= 1
                del polynom[offset + 1:]
        return self

    def search_possible_root(self):
        """
        ищет возможные корни многочлена
        """
        def find_divisors(n):
            n = abs(n)
            divisors = []
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
            return divisors

        div_jun = find_divisors(self[0])
        din_sen = find_divisors(self[-1])
        root1 = set([div1 / div2 for div1, div2 in itertools.product(div_jun, din_sen) if div2 != 0])
        root2 = {-elem for elem in root1}
        return root1 | root2

    def search_root(self):
        """
        Проверяет возможные корни схемой горнера и возвращает корни, прошедшие проверку
        """
        polynom = self.polynom
        roots = []
        while polynom[0] == 0:
            roots.append(0)
            polynom = (Polynom(polynom) / Polynom(0, 1))[0]
        for root in Polynom(polynom).search_possible_root():
            result = polynom[::-1]
            while True:
                for i in range(1, len(result)):
                    result[i] = result[i - 1] * root + result[i]
                if result[-1] == 0:
                    result = result[:-1]
                    roots.append(root)
                else:
                    break
        return roots

    def factorization(self):
        """
        расладывает многочлен на множители вида x - <корень>
        заполняется массив multipliers
        polynom делится на множетели
        """
        while self[0] == 0:
            self.multipliers.append(Polynom(0, 1))
            self.polynom = (self / self.multipliers[-1])[0]
        for root in self.search_possible_root():
            result = Polynom(self[::-1])
            while True:
                for i in range(1, len(self)):
                    result[i] = result[i - 1] * root + result[i]
                if result[-1] == 0:
                    self.multipliers.append(Polynom(-root, 1))
                    result = result[:-1]
                    self.polynom = result[::-1]
                else:
                    break


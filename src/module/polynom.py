import itertools
from collections.abc import Iterable


class Polynom:
    def __init__(self, *args):
        if len(args) == 1:
            val = args[0]
            if isinstance(val, Polynom):
                polynom = val[:]
            elif isinstance(val, Iterable):
                polynom = list(val)
            else:
                polynom = [val + 0]
        else:
            polynom = list(args)
        self._polynom = polynom

    def __getitem__(self, index):
        return self._polynom[index] if self._polynom else 0

    def __setitem__(self, key, value):
        self._polynom[key] = value

    def __eq__(self, val):
        if isinstance(val, Polynom):
            return self._polynom == val._polynom
        else:
            return len(self._polynom) == 1 and self._polynom[0] == val

    def __str__(self):
        res = []
        for index, coef in enumerate(self._polynom):
            coef = coef if coef != 1 else ''
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
        return len(self._polynom)

    def __add__(self, polynomial):
        if not isinstance(polynomial, Polynom):
            return
        res = [a + b for a, b in itertools.zip_longest(self._polynom, polynomial._polynom, fillvalue=0)]
        return self.__class__(res)

    def __sub__(self, val):
        return self.__add__(-val)

    def __neg__(self):
        return self.__class__([-co for co in self._polynom])

    def __mul__(self, polynomial):
        if not isinstance(polynomial, Polynom):
            return Polynom([co * polynomial for co in self._polynom])
        poly1 = polynomial._polynom
        poly2 = self._polynom[:]
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
        remainder = Polynom(self[:])
        while len(remainder) >= len(divisor):
            div_degree = len(remainder) - len(divisor)
            div_coef = int(remainder._polynom[-1]) / int(divisor._polynom[-1])
            quotient[div_degree] = div_coef
            monomial = Polynom([0] * (div_degree + 1))
            monomial[-1] = div_coef
            remainder = (remainder - divisor * monomial).trim()
        return quotient.trim(), remainder

    def function_value(self, x):
        rez = 0
        for i in range(len(self._polynom)):
            rez += self._polynom[i] * x ** i
        return rez

    @staticmethod
    def find_divisors(n):
        n = abs(n)
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    def trim(self):
        """
        убирает страшие нулевые коэффициенты
        """
        polynom = self._polynom[:]
        if polynom:
            offset = len(polynom) - 1
            if polynom[offset] == 0:
                offset -= 1
                while offset >= 0 and polynom[offset] == 0:
                    offset -= 1
                del polynom[offset + 1:]
        return Polynom(polynom)

    def search_possible_root(self):
        """
        ищет возможные корни многочлена
        """
        div_jun = self.find_divisors(self[0])
        din_sen = self.find_divisors(self[-1])
        root1 = set([div1 / div2 for div1, div2 in itertools.product(div_jun, din_sen) if div2 != 0])
        root2 = {-elem for elem in root1}
        return root1 | root2

    def search_root(self):
        """
        Проверяет возможные корни схемой горнера и возвращает корни, прошедшие проверку
        """
        polynom = self._polynom[:]
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
        if len(self) <= 1:
            return [self]
        polynom = Polynom(self[:])
        multipliers = []
        while polynom[0] == 0:
            multipliers.append(Polynom(0, 1))
            polynom = (polynom / multipliers[-1])[0]
        for root in polynom.search_root():
            while True:
                if polynom.function_value(root) == 0:
                    multipliers.append(Polynom(-root, 1))
                    polynom = (polynom/multipliers[-1])[0]
                else:
                    break
        return multipliers

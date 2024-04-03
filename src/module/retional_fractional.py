from polynom import Polynom
from fractions import Fraction


class RationalFraction:
    """
    Класс рациональных дробей, реализующий разложение рац дробей на простешие
    (разложение корректно работает только с 1 и 2 типом простейших дробей)
    """
    def __init__(self, divisible: Polynom, divisor: Polynom, _type=0):
        self.divisible = divisible
        self.divisor = divisor
        self.integer_part = 0
        self.type = _type if 1 <= _type <= 4 and isinstance(_type, int) else 0

    def right_fraction(self):
        """
        Приведение к правильной дроби
        """
        if len(self.divisible) >= len(self.divisor):
            div_polynom = self.divisible / self.divisor
            self.integer_part = div_polynom[0]
            self.divisible = div_polynom[1]

    def get_denominators_simplest_fractions(self):
        """
        Получение списка знаменателей простейших дробей с неизвестными коэффициентами и тип простешей дробт
        :return: список знаменателей простейших дробей
        """
        # Нужно представить вот в таком виде:
        # A/x,B/(x-1),C/(x-1)^2,(Dx+E)/(x^2+x+1) и найти А,B,C,
        prime_fractions = []  # x,(x-1),(x-1)^2,(x^2+x+1)
        for mult in self.divisor.multipliers:
            if mult in prime_fractions:
                prime_fractions.append(prime_fractions[-1] * mult)
                continue
            prime_fractions.append(mult)
        return prime_fractions

    def get_numerator_under_common_fraction(self):
        """
        Получение списка коэфициентов(многочленов) при неизвестных под общим знаменателем с неизвестными коэффициентами
        """
        common_denominator = Polynom([1])
        for mult in self.divisor.multipliers:
            common_denominator *= mult
        prime_fractions = self.get_denominators_simplest_fractions()
        for index in range(len(prime_fractions)):
            prime_fractions[index] = (common_denominator / prime_fractions[index])[0]
        return prime_fractions

    def get_system_linear_equations(self, polynom_a, polynom_b):
        """
        Получение расширенной матрицы системы линейных уравнений с неизвестными кофициентами (AX = B)
        """
        linear_equation = []
        system_linear_equations = []
        for index in range(len(polynom_a)):
            for polynom in polynom_a:
                if len(polynom) <= index:
                    linear_equation.append(0)
                else:
                    linear_equation.append(polynom[index])
            if len(self.divisible) > index:
                linear_equation.append(polynom_b[index])
            else:
                linear_equation.append(0)
            system_linear_equations.append(linear_equation[:])
            linear_equation.clear()
        return system_linear_equations

    def get_simplest_fractions(self):
        """
        разложение рациональной дроби в сумму простеших дробей
        :return: список простеших дробей
        """
        poly_b = self.divisible
        self.divisor.factorization()
        poly_a = self.get_numerator_under_common_fraction()

        matrix = self.get_system_linear_equations(poly_a, poly_b)
        coefficients = gauss_jordan(matrix)
        simplest_fractions = []
        for (coef, index), divisor in zip(coefficients, self.get_denominators_simplest_fractions()):
            simplest_fractions.append(RationalFraction(coef, divisor, 1 if len(divisor) == 2 else 2))
        return simplest_fractions


def gauss_jordan(matrix):
    """
    Решение методом Гаусса-Жордана системы линейных уравнений.
    matrix: двумерный список, расширенную матрицу системы
    Возвращает: решение системы
    """
    matrix = [row[:] for row in matrix]
    index = list(range(len(matrix)))
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        max_row = max(range(i, rows), key=lambda x: abs(matrix[x][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        index[i], index[max_row] = index[max_row], index[i]
        leading_coefficient = matrix[i][i]
        matrix[i] = [element / leading_coefficient for element in matrix[i]]
        for j in range(rows):
            if j != i:
                coefficient = matrix[j][i]
                matrix[j] = [element - coefficient * matrix[i][index] for index, element in enumerate(matrix[j])]

    return [(row[cols - 1], ind) for row, ind in zip(matrix, index)]


a = RationalFraction(
    Polynom(1, 2),
    Polynom(0, 0, 0, 234, 309, 164, 50, 10, 1)
)

for k in a.get_simplest_fractions():
    print(Fraction(float(k.divisible)).limit_denominator(1000), k.divisor, k.type)

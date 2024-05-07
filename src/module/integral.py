from sympy import *

from src.module.polynom import Polynom
from src.module.rational_fractional import RationalFraction


def integrating_polynomial(simpl_frac: Polynom):
    """
    Возвращает интеграл от полинома
    :return Polynom
    """
    if simpl_frac == 0:
        return ""
    polynom = Polynom(0)
    for i in range(len(simpl_frac) - 1, -1, -1):
        coef = simpl_frac[i] / (i + 1)
        coef = int(coef) if coef == int(coef) else coef
        polynom = polynom + Polynom([0 for _ in range(i + 1)] + [coef])
    return polynom


def integration_simplest_fractions(simpl_frac: RationalFraction):
    """
    интеграл от простейшей дроби
    Возвращает кортеж из корня степени и коэффициента
    :return tuple
    """
    multiplier = simpl_frac.divisor.factorization()
    coef = simpl_frac.divisible
    match simpl_frac.type:
        case 1:
            return -multiplier[0][0], '', coef
        case 2:
            return -multiplier[0][0], len(multiplier) - 1, coef / (1 - len(multiplier))


def integral_rational_frac(rational_fraction):
    """
    интеграл рациональной дроби
    собирает сумму простейших дробей в структуру
    return dict
    """
    sum_coefficients = {}
    for simple_frac in rational_fraction.get_simplest_fractions():
        tmp = integration_simplest_fractions(simple_frac)
        key = (tmp[0], tmp[1])
        value = tmp[2]
        if key in sum_coefficients:
            sum_coefficients[key] += value
        sum_coefficients[key] = value
    return sum_coefficients


def function_value_integral_rational_frac(integral_rat_frac: dict, x):
    """
    Значение функции от интеграла рациональной функции
    :return floot
    """
    rez = 0
    for (root, degree), coef in integral_rat_frac.items():
        if x - root == 0:
            raise Exception(f"Вы ввели функцию которая терпит бесконечный разрыв в точке {root}")
        if not degree:
            rez += coef * ln(abs(x - root))
        else:
            rez += coef / (x - root) ** degree
    return rez


def str_integral_simples_frac(integral_rat_frac: dict):
    """
    строковое представление интеграла
    """
    rez = ""
    for (root, degree), coef in integral_rat_frac.items():
        coef = coef if coef != 1 else ''
        sign1 = '+' if coef > 0 else ''
        sign2 = '+' if -root > 0 else ''
        root = int(root) if root == int(root) else root
        root = root if root != 0 else ''
        coef = int(coef) if coef == int(coef) else coef
        if degree == '':
            rez += f"{sign1}{coef}ln(|x{sign2}{-root}|)"
        else:
            if degree == 1:
                rez += f"{sign1}{coef}/(x{sign2}{-root})"
            else:
                rez += f"{sign1}{coef}/(x{sign2}{-root})^{degree}"
    return rez


def indefinite(rational_frac: RationalFraction):
    """
    вывод первообразной
    """
    integer_part = integrating_polynomial(rational_frac.integer_part)
    fractional_part = integral_rational_frac(rational_frac)
    return str(integer_part) + str_integral_simples_frac(fractional_part) + ' + C'


def definite_integral(rational_frac, upper_limit, lower_limit):
    """
    вывод определенного интеграла
    """
    integer_part = integrating_polynomial(rational_frac.integer_part)
    ivalue_upper_point = integer_part.function_value(upper_limit)
    ivalue_lower_point = integer_part.function_value(lower_limit)
    value_integer_part = ivalue_upper_point - ivalue_lower_point

    fractional_part = integral_rational_frac(rational_frac)
    fvalue_upper_point = function_value_integral_rational_frac(fractional_part, upper_limit)
    fvalue_lower_point = function_value_integral_rational_frac(fractional_part, lower_limit)
    value_fractional_part = fvalue_upper_point - fvalue_lower_point
    return value_integer_part + value_fractional_part


def calculate(rational_frac, mode):
    rational_frac.right_fraction()
    if mode == "indefinite":
        return indefinite(rational_frac)
    elif mode == "definite":
        return indefinite(rational_frac)

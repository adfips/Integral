import re


def parsing(in_str):
    """Парсер, который из строки преобразует в два списка: числитель и знаменатель."""
    parth = in_str.split('/')
    if len(parth) == 2:
        numerator_str = parth[0].strip().replace(' ', '')
        denumerator_str = parth[1].strip().replace(' ', '')
        numerator = parse_expression(numerator_str)
        denumerator = parse_expression(denumerator_str)
        return numerator, denumerator
    else:
        numerator_str = parth[0].strip().replace(' ', '')
        numerator = parse_expression(numerator_str)
        return numerator, [1]


def parse_expression(expression):
    """функцияя которая приводит выражение к списку где на на i - ом месте i - ая степень"""
    coefficients = {}

    terms = re.findall(r'(-?\d*)\s*x\^?(\d*)|(-?\d+)', expression)

    for term in terms:
        if term[0] != '' or term[1] != '':
            if term[0] == '-':
                coefficient = -1
            else:
                coefficient = int(term[0]) if term[0] else 1
            power = int(term[1]) if term[1] else 1
        else:
            coefficient = int(term[2]) if term[2] else 1
            power = 0 if term[2] else 1
        if power in coefficients:
            coefficients[power] += coefficient
        else:
            coefficients[power] = coefficient
    if 0 not in coefficients:
        coefficients[0] = 0

    max_power = max(coefficients.keys())
    result = [coefficients.get(power, 0) for power in range(0, max_power + 1)]

    return result

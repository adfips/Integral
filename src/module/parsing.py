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
    elif len(parth) > 2:
        s = "".join([" " * len(i) + '^' for i in parth[:-1]])
        print(f'{in_str}\n{" " * 11 + s}\n'
                        f'Вы указали {len(parth) - 1} знака разделить.'
                        ' Вы должны ввести рациональную дробь с целыми коэфициентами')
        quit(0)
    else:
        numerator_str = parth[0].strip().replace(' ', '')
        numerator = parse_expression(numerator_str)
        return numerator, [1]


def parse_expression(expression: str):
    """функцияя которая приводит выражение к списку где на на i - ом месте i - ая степень"""
    coefficients = {}
    check_exception(expression)
    expression = expression.replace("*", "")
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


def check_exception(expression):
    exception1 = re.findall(r'\d+(?:\*\d+)+', expression)
    if exception1:
        s = " " * (len(expression))
        for i in exception1:
            find = expression.find(i)
            s = s[:find] + "^" * len(i) + s[find:]
            s = f'{expression}\n{" " * 11 + s}\n'
        print(s + "за место этих выражений нужно написать их значение: " + f", ".join(exception1))
        quit(0)
    if expression[0] == '(':
        if expression[-1] != ')':
            s = f'{expression}\n{" " * (11 + len(expression))}^\n'
            print(s + "Вы не закрыли скобку")
            quit(0)
    else:
        if expression[-1] == ')':
            s = f'{expression}\n{" " * 10}^\n'
            print(s + "Вы не открыли скобку")
            quit(0)

    expression = expression[1:-1]
    if expression.count('(') > 0 or expression.count(')') > 0:
        s = "^".join([" " * len(i) for i in re.split(r'[()]', expression)])
        s = f'{expression}\n{" " * 11 + s}\n'
        print(s + "Вычислите выражение в скобках")
        quit(0)

    exception2 = re.split(r'[0-9x]', expression)
    for i in exception2:
        if len(i) > 1 or i not in "+-*^":
            s = " " * expression.find(i) + "^" * len(i)
            s = f'{expression}\n{" " * 11 + s}\n'
            print(s + "некорректный ввод")
            quit(0)

    exception3 = re.split(r'x+(?:\*x+)+|x{2,}', expression)
    if len(exception3) != 1:
        s = "^^".join([" " * len(i) for i in exception3])
        s = f'{expression}\n{" " * 11 + s}\n'
        print(s + "некорректный ввод")
        quit(0)
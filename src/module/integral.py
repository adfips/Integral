from sympy import *


class Integral:
    def __init__(self, simpl_frac):
        multiplier = simpl_frac.divisor.multipliers
        coef = Rational(simpl_frac.divisible).limit_denominator(1000)
        integer_part = simpl_frac.integer_part
        self.integral = 0
        x = Symbol('x')
        if integer_part != 0:
            for i in range(len(integer_part) - 1, -1, -1):
                self.integral += Rational(integer_part[i] / (i + 1)).limit_denominator(100) * x ** (i + 1)
        match simpl_frac.type:
            case 1:
                self.integral = coef * ln(x - multiplier[0][0])
            case 2:
                self.integral = coef / ((1 - len(multiplier)) * (x - multiplier[0][0]) ** (len(multiplier) - 1))
            case 3:
                pass
            case 4:
                pass

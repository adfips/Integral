from sympy import *

from src.module.polynom import Polynom


class Integral:
    def __init__(self, simpl_frac):
        x = Symbol('x')
        self.integral = Symbol('C')
        if isinstance(simpl_frac, Polynom):
            if simpl_frac != 0:
                for i in range(len(simpl_frac) - 1, -1, -1):
                    self.integral += Rational(simpl_frac[i] / (i + 1)).limit_denominator(100) * x ** (i + 1)
                return
        multiplier = simpl_frac.divisor.multipliers
        coef = Rational(simpl_frac.divisible).limit_denominator(1000)

        match simpl_frac.type:
            case 1:
                self.integral = coef * ln(x - multiplier[0][0])
            case 2:
                self.integral = coef / ((1 - len(multiplier)) * (x - multiplier[0][0]) ** (len(multiplier) - 1))
            case 3:
                pass
            case 4:
                pass

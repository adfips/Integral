from polynom import Polynom


class RationalFraction:
    def __init__(self, divisible: Polynom, divisor: Polynom):
        self.divisible = divisible
        self.divisor = divisor
        self.integer_part = 0

    def right_fraction(self):
        if len(self.divisible) >= len(self.divisor):
            div_polynom = self.divisible / self.divisor
            self.integer_part = div_polynom[0]
            self.divisible = div_polynom[1]



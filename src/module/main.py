from src.module.integral import Integral
from src.module.parsing import parsing
from src.module.polynom import Polynom
from rational_fractional import RationalFraction


def main():
    input_str = "(1-x-3x^2++1x^3)/(x^2-1)"
    frac = parsing(input_str)
    a = RationalFraction(
        Polynom(frac[0]),
        Polynom(frac[1])
    )
    print(a.divisible)
    print(a.divisor)
    a.right_fraction()
    print(a.integer_part)
    print(a.divisible)
    print(a.divisor)
    rez = str(Integral(a.integer_part).integral)
    print(rez)
    q = a.get_simplest_fractions()
    for k in a.get_simplest_fractions():
        b = Integral(k).integral
        rez = rez + str(Integral(k).integral)
    print(rez)


if __name__ == '__main__':
    main()

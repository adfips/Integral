from src.module.integral import *
from src.module.parsing import parsing
from src.module.polynom import Polynom
from rational_fractional import RationalFraction


def main():
    input_str = "(1+x-3x^2+1x^3)/(x^3+3x^2+3x+1)"
    frac = parsing(input_str)
    a = RationalFraction(
        Polynom(frac[0]),
        Polynom(frac[1])
    )
    a.right_fraction()
    print(antiderivative(a))
    print(definite_integral(a, 1, 0))


if __name__ == '__main__':
    main()

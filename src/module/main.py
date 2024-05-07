from src.module.integral import *
from src.module.parsing import parsing
from src.module.polynom import Polynom
from rational_fractional import RationalFraction


def main():
    input_str = "(1+1x-7*x^4+1x^3)/(x^3+3x^2+3x+1)"
    frac = parsing(input_str)
    a = RationalFraction(
        Polynom(frac[0]),
        Polynom(frac[1])
    )
    print(calculate(a, "indefinite"))


if __name__ == '__main__':
    main()

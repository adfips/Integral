from src.module.integral import calculate
from src.module.parsing import parsing
from src.module.polynom import Polynom
from src.module.rational_fractional import RationalFraction
from sys import argv


def main():
    if len(argv) == 1:
        quit(0)
    elif len(argv) >= 2:
        frac = parsing(argv[1])
        a = RationalFraction(
            Polynom(frac[0]),
            Polynom(frac[1])
        )
        print(calculate(a, "-indef" if len(argv) == 2 else argv[2]))
    else:
        quit(0)


if __name__ == '__main__':
    main()

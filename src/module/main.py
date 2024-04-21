from src.module.integral import Integral
from src.module.parsing import parsing
from src.module.polynom import Polynom
from src.module.rational_fractional import RationalFraction

input_str = "(234x^3+309x^4+164x^5+50x^6+10x^7+x^8)"
frac = parsing(input_str)
print(frac[0], frac[1])
a = RationalFraction(
    Polynom(frac[0]),
    Polynom(frac[1])
)
a.right_fraction()
print(a.integer_part)
rez = Integral(a.integer_part).integral
for k in a.get_simplest_fractions():
    k.divisor.factorization()
    rez += Integral(k).integral
print(rez)

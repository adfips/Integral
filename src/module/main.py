from src.module.integral import Integral
from src.module.polynom import Polynom
from src.module.rational_fractional import RationalFraction

a = RationalFraction(
    Polynom(1, 2),
    Polynom(0, 0, 0, 234, 309, 164, 50, 10, 1)
)
a.right_fraction()
rez = 0
for k in a.get_simplest_fractions():
    k.divisor.factorization()
    rez += Integral(k).integral
print(rez)

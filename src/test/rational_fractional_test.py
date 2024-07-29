import unittest

from src.module.polynom import Polynom
from src.module.rational_fractional import RationalFraction


class MyTestCase(unittest.TestCase):
    def test_right_fraction(self):
        rational_frac = RationalFraction(Polynom(1), Polynom(0, 1))
        rational_frac.right_fraction()
        self.assertEqual(rational_frac.divisible, 1)
        self.assertEqual(rational_frac.divisor, Polynom(0, 1))
        self.assertEqual(rational_frac.integer_part, 0)

    def test_get_denominators_simplest_fractions(self):
        rational_frac = RationalFraction(Polynom(1, 2, 3, 4, 3, 2, 1), Polynom(1, 2, 1))
        self.assertEqual(
            rational_frac.get_denominators_simplest_fractions(),
            [Polynom(1, 1), Polynom(1, 2, 1)]
        )

    def test_get_numerator_under_common_fraction(self):
        rational_frac = RationalFraction(Polynom(1), Polynom(1, 2, 1))
        self.assertEqual(rational_frac.get_numerator_under_common_fraction(), [Polynom(1, 1), Polynom(1)])

    def test_get_system_linear_equations(self):
        rational_frac = RationalFraction(Polynom(4, 2), Polynom(-1, 0, 1))
        test = RationalFraction.get_system_linear_equations(rational_frac.get_numerator_under_common_fraction(),
                                                            Polynom(4, 2))
        self.assertEqual(test, [[1, -1, 4], [1, 1, 2]])

    def test_gauss_jordan(self):
        rational_frac = RationalFraction(Polynom(4, 2), Polynom(-1, 0, 1))
        matrix = RationalFraction.get_system_linear_equations(rational_frac.get_numerator_under_common_fraction(),
                                                              Polynom(4, 2))
        self.assertEqual(rational_frac.gauss_jordan(matrix), [(3, 0), (-1, 1)])

    def test_get_simplest_fractions(self):
        rational_frac = RationalFraction(Polynom(4, 2), Polynom(-1, 0, 1))
        rational_frac_test1 = RationalFraction(Polynom(3.0), Polynom(-1.0, 1), 1)
        rational_frac_test2 = RationalFraction(Polynom(-1.0), Polynom(1.0, 1), 1)
        a = rational_frac.get_simplest_fractions()
        self.assertEqual([a[0].divisor, a[0].divisible],
                         [rational_frac_test1.divisor, rational_frac_test1.divisible])
        self.assertEqual([a[1].divisor, a[1].divisible],
                         [rational_frac_test2.divisor, rational_frac_test2.divisible])


if __name__ == '__main__':
    unittest.main()

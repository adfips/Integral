import unittest

from src.module.polynom import Polynom


class MyTestCase(unittest.TestCase):

    def test__init__(self):
        poly = Polynom()
        self.assertEqual(poly._polynom, [])
        poly = Polynom(0)
        self.assertEqual(poly._polynom, [0])
        poly = Polynom(0, )
        self.assertEqual(poly._polynom, [0])
        poly = Polynom(1, 2, 3)
        self.assertEqual(poly._polynom, [1, 2, 3])
        poly = Polynom([])
        self.assertEqual(poly._polynom, [])
        poly = Polynom([1, 2, 3])
        self.assertEqual(poly._polynom, [1, 2, 3])
        poly = Polynom(poly)
        self.assertEqual(poly._polynom, [1, 2, 3])
        poly = Polynom(0, 0, 0, 0)
        self.assertEqual(poly._polynom, [0, 0, 0, 0])

    def test__getitem__(self):
        poly = Polynom(0)
        self.assertEqual(poly[0], 0)
        poly = Polynom([])
        self.assertEqual(poly[0], 0)
        poly = Polynom()
        self.assertEqual(poly[0], 0)
        poly = Polynom(1, 2, 3)
        self.assertEqual(poly[-1], 3)

    def test__setitem__(self):
        poly = Polynom(0)
        poly[0] = 1
        self.assertEqual(poly[0], 1)

    def test__eq__(self):
        poly = Polynom(1, 2, 0, 0)
        self.assertEqual(poly == Polynom(1, 2, 0, 0), True)
        self.assertEqual(poly == Polynom(1, 2), False)
        poly = Polynom()
        self.assertEqual(poly == [], False)
        poly = Polynom(1234)
        self.assertEqual(poly == 1234, True)

    def test__str__(self):
        poly1 = Polynom([1, 2, 3, 4])
        poly2 = Polynom([1, 0, 1, 0, -0, --1])
        self.assertEqual(str(poly1), "4X^3 + 3X^2 + 2X + 1")
        self.assertEqual(str(poly2), "1X^5 + 1X^2 + 1")

    def test__len__(self):
        self.assertEqual(len(Polynom(1, 2, 3, 4)), 4)

    def test__add__(self):
        poly1 = Polynom([1, 2, 3, 4])
        poly2 = Polynom([1, 2, 0, -4, 1, 2, 3])
        self.assertEqual((poly1 + poly2), Polynom([2, 4, 3, 0, 1, 2, 3]))

    def test__sub__(self):
        poly1 = Polynom(1, 2, 3, 4)
        poly2 = Polynom(2, 3, 4, 5)
        self.assertEqual((poly1 - poly2), Polynom([-1, -1, -1, -1]))

    def test__neg__(self):
        self.assertEqual((-Polynom(1, 2, 3, 4))._polynom, [-1, -2, -3, -4])

    def test__mul__(self):
        poly1 = Polynom(-5, 2, 8, -3, -3, 0, 1, 0, 1)
        poly2 = Polynom(21, -9, -4, 0, 5, 0, 3)
        self.assertEqual(
            (poly2 * poly1),
            Polynom([-105, 87, 170, -143, -93, 49, 58, -18, 26, -18, -8, 0, 8, 0, 3])
        )

    def test__pow__(self):
        poly = Polynom(0, 1) ** 3
        self.assertEqual(poly._polynom, [0, 0, 0, 1])
        poly = Polynom(5, 4, 3, 2, 1) ** 5
        self.assertEqual(poly._polynom,
                         [3125, 12500, 29375, 52250, 76775, 96224, 105490, 102820, 89905, 70860,
                          50553, 32670, 19085, 10040, 4730, 1972, 715, 220, 55, 10, 1])

    def test__truediv__(self):
        poly1 = Polynom(-105, 87, 170, -143, -93, 49, 58, -18, 26, -18, -8, 0, 8, 0, 3)
        poly2 = Polynom(21, -9, -4, 0, 5, 0, 3)
        self.assertEqual((poly1 / poly2)[0], Polynom(-5, 2, 8, -3, -3, 0, 1, 0, 1))
        self.assertEqual((poly1 / poly2)[1], Polynom())

    def test_find_divisors(self):
        self.assertEqual(
            Polynom.find_divisors(39), [1, 39, 3, 13]
        )
        self.assertEqual(
            Polynom.find_divisors(0), []
        )
        self.assertEqual(
            Polynom.find_divisors(139), [1, 139]
        )
        self.assertEqual(
            Polynom.find_divisors(1), [1]
        )

    def test_trim(self):
        poly1 = Polynom([1, 0, 2, 0, 0, 0.1, 0, 0])
        poly2 = Polynom([0, 0])
        self.assertEqual(poly1.trim(), Polynom([1, 0, 2, 0, 0, 0.1]))
        self.assertEqual(poly2.trim(), Polynom())

    def test_search_possible_root(self):
        poly = Polynom(1, 2, 4, 5, 17)
        self.assertEqual(poly.search_possible_root(), {1 / 17, 1, -1 / 17, -1})

    def test_search_root(self):
        poly = Polynom(0, 0, 0, 1)
        self.assertEqual(poly.search_root(), [0, 0, 0])
        poly = Polynom(1, 1, 1, 1)
        self.assertEqual(poly.search_root(), [-1])
        poly = Polynom(10, 20, 30, 11)
        self.assertEqual(poly.search_root(), [])

    def test_factorization(self):
        self.assertEqual(Polynom().factorization(), [Polynom()])
        self.assertEqual(Polynom(123).factorization(), [Polynom(123)])
        poly = Polynom(1, 3, 3, 1).factorization()
        self.assertEqual(poly, [Polynom(1, 1), Polynom(1, 1), Polynom(1, 1)])


if __name__ == '__main__':
    unittest.main()

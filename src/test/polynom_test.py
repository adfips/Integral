import unittest

from src.module.polynom import Polynom


class MyTestCase(unittest.TestCase):
    def test_str(self):
        poly1 = Polynom([1, 2, 3, 4])
        poly2 = Polynom([1, 0, 1, 0, -0, --1])
        self.assertEqual(str(poly1), "4X^3 + 3X^2 + 2X + 1")
        self.assertEqual(str(poly2), "1X^5 + 1X^2 + 1")

    def test_add(self):
        poly1 = Polynom([1, 2, 3, 4])
        poly2 = Polynom([1, 2, 0, -4, 1, 2, 3])
        self.assertEqual((poly1 + poly2).polynom, Polynom([2, 4, 3, 0, 1, 2, 3]).polynom)

    def test_sub(self):
        poly1 = Polynom(1, 2, 3, 4)
        poly2 = Polynom(2, 3, 4, 5)
        self.assertEqual((poly1 - poly2).polynom, [-1, -1, -1, -1])

    def test_mul(self):
        poly1 = Polynom(-5, 2, 8, -3, -3, 0, 1, 0, 1)
        poly2 = Polynom(21, -9, -4, 0, 5, 0, 3)
        self.assertEqual(
            (poly2 * poly1).polynom,
            [-105, 87, 170, -143, -93, 49, 58, -18, 26, -18, -8, 0, 8, 0, 3]
        )

    def test_truediv(self):
        poly1 = Polynom(-105, 87, 170, -143, -93, 49, 58, -18, 26, -18, -8, 0, 8, 0, 3)
        poly2 = Polynom(21, -9, -4, 0, 5, 0, 3)
        self.assertEqual((poly1 / poly2)[0].polynom, [-5, 2, 8, -3, -3, 0, 1, 0, 1])
        self.assertEqual((poly1 / poly2)[1].polynom, [])

    def test_trim(self):
        poly1 = Polynom(1, 0, 2, 0, 0, 0.1, 0, 0)
        poly2 = Polynom(0, 0)
        poly1.trim()
        poly2.trim()
        self.assertEqual(poly1.polynom, [1, 0, 2, 0, 0, 0.1])
        self.assertEqual(poly2.polynom, [])

    def test_search_possible_root(self):
        poly = Polynom(1, 2, 4, 5, 17)
        self.assertEqual(poly.search_possible_root(), {1 / 17, 1, -1 / 17, -1})


if __name__ == '__main__':
    unittest.main()

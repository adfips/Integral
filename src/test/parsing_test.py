import unittest

from src.module.parsing import parsing as ps, parse_expression as pr


class ParsingTest(unittest.TestCase):
    """Класс тестирующий основную функциюю парсинга"""

    def test_just_fraction(self):
        example = '2x + 1 -1'
        exc = [0, 2]
        self.assertEqual((exc, [1]), ps(example))

    def test_default_fraction(self):
        example = '2x + 1 - 1 /2x + 1 - 1'
        exc = [0, 2], [0, 2]
        self.assertEqual(exc, ps(example))

    def test_large_similar_syllables(self):
        example = '2x + 18x - 14x - 12 + 10/27x^2 - 2x^2 + 12x - 4x - 10'
        exc = [-2, 6], [-10, 8, 25]
        self.assertEqual(exc, ps(example))

    def test_more_degree(self):
        example = '17x^4-103x^4-12x+15x^3-300x^2+12x/67-2015x^5-77x^2+5'
        exc = [0, 0, -300, 15, -86], [72, 0, -77, 0, 0, -2015]
        self.assertEqual(exc, ps(example))


class AlsoFunctionTest(unittest.TestCase):
    """Класс тестирующий вспомогоательные функции парсинга"""

    def test_parse_excpression(self):
        example = '12x^3+14x^3+12x+6x-10+10+2'
        exc = [2, 18, 0, 26]
        self.assertEqual(exc, pr(example))

    def test_big_excpression(self):
        example = '12x^7+37x^6-1387913x^6+3214x^4+201111x-1288012+23123-20134'
        exc = [-1285023, 201111, 0, 0, 3214, 0, -1387876, 12]
        self.assertEqual(exc, pr(example))


if __name__ == '__main__':
    unittest.main()

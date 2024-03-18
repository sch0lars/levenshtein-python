import levenshtein
import unittest


class Test(unittest.TestCase):
    def test_class_different_values_1(self):
        a = 'horse'
        b = 'rose'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 2)

    def test_class_different_values_2(self):
        a = 'hello'
        b = 'world'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 4)

    def test_class_different_values_3(self):
        a = '1234'
        b = '0135'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 3)

    def test_class_different_values_4(self):
        a = '!!@@#$$$'
        b = '@!#$$$$'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 4)

    def test_class_same_values_1(self):
        a = 'test'
        b = 'test'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 0)

    def test_class_same_values_2(self):
        a = '123'
        b = '123'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 0)

    def test_class_same_values_3(self):
        a = '0000'
        b = '0000'
        lm = levenshtein.LevenshteinMatrix(a, b)
        self.assertEqual(lm.get_distance(), 0)

    def test_get_distance_different_values_1(self):
        a = '1234'
        b = '4321'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 4)

    def test_get_distance_different_values_2(self):
        a = 'foo'
        b = 'foobar'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 3)

    def test_get_distance_different_values_3(self):
        a = 'rose'
        b = 'horse'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 2)

    def test_get_distance_same_values_1(self):
        a = 'test'
        b = 'test'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 0)

    def test_get_distance_same_values_2(self):
        a = '123'
        b = '123'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 0)

    def test_get_distance_same_values_3(self):
        a = '!@#$%^&*()'
        b = '!@#$%^&*()'
        distance = levenshtein.get_distance(a, b)
        self.assertEqual(distance, 0)

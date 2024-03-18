import levenshtein
import unittest


class Test(unittest.TestCase):
    def test_instance_incorrect_arguments(self):
        '''Test for incorrect arguments when instantiating object'''
        with self.assertRaises(TypeError):
            levenshtein.LevenshteinMatrix('test', 5)

    def test_get_distance_incorrect_arguments(self):
        '''Test for incorrect arguments when calling `get_distance()`'''
        with self.assertRaises(TypeError):
            levenshtein.get_distance('test', 5)

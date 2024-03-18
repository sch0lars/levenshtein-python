from typing import List


class LevenshteinMatrix:
    def __init__(self, a: str, b: str):
        '''
        Constructs a Levenshtein matrix for two strings, `a` and `b`

        :param a: the first string for which to get the edit distance
        :param b: the second string for which to get the edit distance

        :returns: a LevenshteinMatrix object
        :raises TypeError: if arguments are not strings
        '''
        # Ensure we get two strings as arguments
        if not all(isinstance(arg, str) for arg in (a, b)):
            raise TypeError(
                f"Expected arguments 'str', 'str'; got '{type(a).__name__}', '{type(b).__name__}'")
        self._a: str = a
        self._b: str = b
        self._matrix: List[List[int]] = self._generate_matrix()
        # Create an instance method for obtaining the distance
        self.get_distance = lambda: self._matrix[-1][-1]

    def _get_min(self, x: int, y: int, matrix: List[List[int]]):
        '''
        Get the minimum value of the tail values of a `matrix` at coordinates (`x`, `y`)

        :param x:
        :param y:
        :param matrix:

        :returns: the minimum value of the tail values
        :raises IndexError: if the coordinate (`x`, `y`) is out of range
        '''
        a = matrix[x][y-1]
        b = matrix[x-1][y]
        c = matrix[x-1][y-1]

        return min(a, b, c) + 1 if self._a[y-1] != self._b[x-1] else c

    def _generate_matrix(self) -> List[List[int]]:
        '''
        Generate the Levenshtein matrix

        :returns: a two-dimensional list representing the Levenshtein matrix
        '''
        # Get the length and width of the numbers, and add 1 for the empty string
        length: int = len(self._b) + 1
        width: int = len(self._a) + 1
        # Initialize an empty list for the matrix
        matrix: List[List[int]] = [[0 for i in range(width)]
                                   for j in range(length)]

        # Populate the initial rows
        for i in range(width):
            matrix[0][i] = i
        # Populate the initial columns
        for i in range(length):
            matrix[i][0] = i

        # Fill in the remaining rows and columns
        for i in range(1, length):
            for j in range(1, width):
                matrix[i][j] = self._get_min(i, j, matrix)

        return matrix

    def print_matrix(self) -> None:
        '''
        Print the Levenshtein matrix

        :returns: None
        '''
        # Print the first word, including the space
        for c in ' ' * 2 + self._a:
            print(c, end=' ')
        print()
        # Print the column letters and the matrix values
        word = ' ' + self._b
        for i, row in enumerate(self._matrix):
            print(word[i], end=' ')
            for cell in row:
                print(cell, end=' ')
            print()


def get_distance(a: str, b: str) -> int:
    '''
    Calculate the Levenshtein distance between two strings, `a` and `b`

    :param a: the first string for which to get the edit distance
    :param b: the second string for which to get the edit distance

    :returns: the Levenshtein distance between `a` and `b`
    :raises TypeError: if arguments are not strings
    '''
    # Ensure we get two strings as arguments
    if not all(isinstance(arg, str) for arg in (a, b)):
        raise TypeError(
            f"Expected arguments 'str', 'str'; got '{type(a).__name__}', '{type(b).__name__}'")

    return LevenshteinMatrix(a, b).get_distance()

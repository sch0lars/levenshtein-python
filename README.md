# levenshtein-python

`levenshtein-python` is a Python library which calculates the Levenshtein distance, also known as the edit distance, between two strings.

## Usage

There are two ways of retrieving the Levenshtein distance:
1. Creating a `LevenshteinMatrix` object
   - This has the added benefit of printing the edit matrix via the `print_matrix()` method
2. Calling the `get_distance()` function

### Creating a `LevenshteinMatrix` Object

```python
a = 'horse'
b = 'rose'
lm = LevenshteinMatrix(a, b)
distance = lm.get_distance()
```
This will assign the value `2` to the variable `distance`.

Using the `LevenshteinMatrix` class instance, you can also call `lm.print_matrix()`, which will print the Levenshtein matrix:
```
    h o r s e
  0 1 2 3 4 5
r 1 1 2 2 3 4
o 2 2 1 2 3 4
s 3 3 2 2 2 3
e 4 4 3 3 3 2
```

### Using the `get_distance()` Function

If you just want to calculate the edit distance, you can call the function `get_distance()` without creating a `LevenshteinMatrix` class instance:
```python
a = 'horse'
b = 'rose'
distance = get_distance(a, b)
```

This will also assign the value `2` to the variable `distance`.

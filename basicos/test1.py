def suma(a, b):
    """Calcula la suma de dos números

    >>> print(suma(1, 2))
    3
    """
    return a + b

import doctest
doctest.testmod()   # automatically validate the embedded tests

print(suma(5, 6))
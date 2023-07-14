import doctest

def mul(a, b):
    """
    >>> mul(3, 5)
    15
    >>> mul('T', 6)
    'TTTTTT'
    """
    return a * b

def add(a, b):
    """
    >>> add(3, 7)
    8
    >>> add('T', 'X')
    'TX'
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()


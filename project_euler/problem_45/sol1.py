"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle	 	T(n) = (n * (n + 1)) / 2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	P(n) = (n * (3 * n − 1)) / 2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	H(n) = n * (2 * n − 1)	 	1, 6, 15, 28, 45, ...
It can be verified that T(285) = P(165) = H(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
All trinagle numbers are hexagonal numbers.
T(2n-1) = n * (2 * n - 1) = H(n)
So we shall check only for hexagonal numbers which are also pentagonal.
"""


def hexagonal_num(n: int) -> int:
    """
    Returns nth hexagonal number
    >>> hexagonal_num(143)
    40755
    >>> hexagonal_num(21)
    861
    >>> hexagonal_num(10)
    190
    """
    return n * (2 * n - 1)


def is_pentagonal(n: int) -> bool:
    """
    Returns True if n is pentagonal, False otherwise.
    >>> is_pentagonal(330)
    True
    >>> is_pentagonal(7683)
    False
    >>> is_pentagonal(2380)
    True
    """
    root = (1 + 24 * n) ** 0.5
    return ((1 + root) / 6) % 1 == 0


def compute_num(start: int = 144) -> int:
    """
    Returns the next number which is traingular, pentagonal and hexagonal.
    >>> compute_num(144)
    1533776805
    """
    n = start
    num = hexagonal_num(n)
    while not is_pentagonal(num):
        n += 1
        num = hexagonal_num(n)
    return num


if __name__ == "__main__":
    print(f"{compute_num(144)} = ")

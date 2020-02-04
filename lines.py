def intersect(x1: float, x2: float, x3: float, x4: float) -> bool:
    """
    Evaluates if two lines overlap.
    Lines (x1, x2) and (x3, x4) must have a minimum length of 1.
    Time Complexity: O(1).
    Space Complexity: O(1).
    :param x1: Numeric initial/end point in line (x1, x2).
    :param x2: Numeric initial/end point in line (x1, x2), x2 is end point if greater than x1.
    :param x3: Numeric initial/end point in line (x3, x4).
    :param x4: Numeric initial/end point in line (x3, x4), x4 is end point if greater than x3.
    :return: True if lines overlap or are equal, False otherwise.
    """
    a, b = min(x1, x2), max(x1, x2)
    c, d = min(x3, x4), max(x3, x4)
    return a != b and c != d and (a <= c <= b or c <= a <= d)

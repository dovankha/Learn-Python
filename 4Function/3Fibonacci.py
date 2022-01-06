def fibonacci(n: int) -> int:
    """Return the 'n'th Fibonacci number, for possible 'n'."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for index in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


def fibonacci1(n: int) -> int:
    """Return the 'n'th Fibonacci number, for possible 'n'."""
    if 0 <= n <= 1:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


for i in range(10):
    print(i, fibonacci1(i))

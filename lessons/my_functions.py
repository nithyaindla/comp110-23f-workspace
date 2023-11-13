"""Things I'll be Importing."""


def addition(x: int, y: int) -> int:
    """Adds x and y."""
    return x + y


def f(x: int) -> int:
    """f doubles x."""
    x *= 2
    print(x)
    return x


y: int = f(3)

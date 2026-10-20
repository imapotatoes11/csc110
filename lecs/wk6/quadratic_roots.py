def quadratic_largest_root(a: float, b: float, c: float) -> float:
    """Return the largest root of ax^2 + bx + c = 0

    Pre-condition: b**2 - 4*a*c >= 0; a != 0
    Post-condition: Returns a real number
    """
    discriminant = b**2 - 4*a*c
    return (-b + discriminant**0.5) / (2*a)

# prof sol
def quadratic_largest_root(a: float, b: float, c: float) -> float:
    """Return the largest real root of the parabola defined by...

    Preconditions: a != 0, and b**2 - 4*a*c <= 0
    Postconditions: returns the largest real root of ...
    """
    discriminant = b**2 - 4*a*c
    return (-b + discriminant**0.5) / (2*a)

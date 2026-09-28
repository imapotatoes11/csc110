
bottom_of_range = -3
top_of_range = 3
increment = 0.25

def f(x, y):
    return 2 ** x - x - 3

desired_precision = 10 ** -3

while bottom_of_range < top_of_range:
    a = bottom_of_range
    b = bottom_of_range + increment


    if f(a) * f(b) < 0:
        while (b - a) > desired_precision:
            midpoint = (a + b) / 2
            if f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        root = (a + b) / 2
        print(root)

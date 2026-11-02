def digit_sum(n: int) -> int:
    #a = n
    #while a % 10 != a:
    #    a = sum([int(i) for i in f"{a}"])
    #return n + a
    return sum([ord(i) for i in f"{n}"])

import matplotlib.pyplot as plt
x = list(range(0, 301))
y = [digit_sum(xa) for xa in x]
plt.plot(x,y)
plt.savefig("graph2.png")

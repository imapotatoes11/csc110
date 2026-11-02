
import math
a = lambda a : eval(f"{chr(0b1100001)}{chr(38 - 1)}{int(math.pi * 100) + 46}")

print(a(400))
print(a(-30))

import matplotlib.pyplot as plt
x = list(range(-1000, 1000))
y = [a(x) for x in x]
plt.plot(x,y)
plt.savefig("graph.png")

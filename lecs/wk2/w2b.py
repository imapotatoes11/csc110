# Version 0
x = 42
is_x_positive = x > 0
y = is_x_positive * "Positive" + (not is_x_positive) * "Negative or Zero"
print(y)

# Version 1
x = 42
if x > 0:
    y = "Positive"
else:
    y = "Negative or Zero"
print(y)

# Version 2
x = 42
y = "Negative or Zero"
if x > 0:
    y = "Positive"
print(y)
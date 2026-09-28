# 1
x = 10
while x > 0:
  print(f"{x}!")
  x -= 1
print("Happy New (School) Year!")

# 2
str = "Welcome to 2026!"
str = "Happy New Year!"
i = 0
number = False
while i < len(str) and not number:
  if str[i] in "0123456789":
    number = True
  i += 1
print(number)

# 2 oneliner
print(any([i.isdigit() for i in str]))

# prof solution 2
mystr = "Welcome to Fall 2026!"
print(mystr)
index = 0
#     (this is a guard ) <- prevents overindexing/IndexError
while index < len(mystr) and not mystr[index].isdigit():
  index += 1
print(index != len(mystr))

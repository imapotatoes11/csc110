# For positive integers x < y, determine how many multiples of 3 that are larger than x but less than y.

x = 5
y = 12
count = 0
for i in range(x + 1, y):
    if i % 3 == 0: count += 1
print(count)

print(sum([int(i % 3 == 0) for i in range(x + 1,y)]))

# pro foslution is same as my lines 3-8

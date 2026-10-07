S = [2,3,5,7,11,13,17,19]
T = [2,4,6,8,10,12,14,16,18]

result = []
for x in S:
  if x in T:
    result.append(x)
print(result)

# list comp:
print([i for i in S if i in T])

# is the intersection of these sets empty?
print(not [i for i in S if i in T])

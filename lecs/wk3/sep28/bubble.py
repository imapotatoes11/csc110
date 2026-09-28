L = [5, 8, 2, 4, 9, 3]

for start_index in range(len(L)):
  for index in range(start_index, len(L)):
    if L[index] < L[start_index]:
      L[index], L[start_index] = L[start_index], L[index]

print(L)

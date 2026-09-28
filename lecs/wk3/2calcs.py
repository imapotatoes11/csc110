left = -2.9
right = -2.8
midpoint = (left + right) / 2
function = 2 ** midpoint - midpoint - 3
while abs(function) > 10 ** -8:
  if function > 0:
    left = midpoint
  else:
    right = midpoint
  midpoint = (left + right) / 2
  function = 2 ** midpoint - midpoint - 3

print(f"Root: {midpoint}")
# sol1 has no guarantees on runtime (?)

# sol2, is more predictable
right = -2.8
left = -2.9
num_iterations = 0
while right - left > 10**-8:
  mid = (left + right) / 2
  result = (2**mid - mid - 3)
  if result < 0:
    right = mid
  else:
    left = mid
  num_iterations += 1
print('Aprox of Root is:',(left + right) / 2,"took this many iterations:",num_iterations)

a,b,c = 3,4,5
triangle_case_1 = "Invalid"
if a + b > c and a + c > b and b + c > a:
  if len(set([a,b,c])) == 2:
    triangle_case_1 = "Isosceles"
  elif len(set([a,b,c])) == 1:
    triangle_case_1 = "Equilateral"
  else:
    triangle_case_1 = "Scalene"
print(triangle_case_1)

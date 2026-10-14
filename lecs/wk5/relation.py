A = {2,3,4,6,9}
B = A
R = {(2,4),(4,2),(3,6),(6,3),(4,6),(6,4),(6,9),(9,6),
     (2,2),(3,3),(4,4),(6,6),(9,9)}


# reflexivity of R
print("is reflexive?", all([(a,a) in R for a in A]))
# Symmetricity of R
#print("is symmetric?", all([dict(R)[a] in dict(R) for a in A])) # ?
print("is symmetric?", all([(b,a) in R for (a,b) in R]))
# transitivity of R
# if (a,b) and (b,c) in R, (a,c) in R
print("is transitive?", all([(a,d) in R for (a,b) in R for (c,d) in R if b == c]))

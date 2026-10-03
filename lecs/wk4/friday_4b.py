# 1
x = "\t  cyclophosphamide, doxorubicin ,prdnisone  "
ls = x.strip().replace(' ','').split(",")
ls = [i.strip() for i in x.split(",")]
print(ls)

#2
raw_tags = [" #Python ", "DATASCIENCE", " machine-learning "]
tags = [i.replace(" ","").lower() for i in raw_tags]
print(tags)

#3
string = "abcd"
string_reverse = "".join([string[i] for i in range(len(string) - 1, -1, -1)])
print(string_reverse)

#4
s = "national aeronatics and space administration"
acronym = "".join([i[0] for i in s.split() if i not in ("and",)])
print(acronym)

#5
str1 = "abcd"
str2 = "abcde"
inter = "".join([i + j for i,j in zip(str1,str2)]) + (str1[len(str2):] if len(str1) > len(str2) else str2[len(str1):])
print(inter)

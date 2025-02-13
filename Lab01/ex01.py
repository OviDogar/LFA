# exercitiul 1

A={"a","b","c"}
B={"x","y","z"}
C={"1","2","3"}

def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)


s1A="ababa"
s2B="xyxyx"
s3C="12321"

print(concatenate(s1A, s2B))
print(invers(s1A))
print(substituie(s1A, "a", "x"))
print(lungime(s1A))
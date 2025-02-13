# exercitiul 2

def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)



ep1={"0","1","2","3","4","5","6","7","8","9"}
ep2={"a","b","c","d","e","f","g","i","j","k"}
ep3={"x1","y1","x2","y2","x3","y3","x4","y4","x5","y5"}

def s1concat2(s1, s2):
    return concatenate(s2, s1)


class MyString:
    def __init__(self, s):
        self.s = s

    def __xor__(self, n):
        if isinstance(n, int) and n >= 0:
            return self.s * n
        raise ValueError("Exponentul trebuie sa fie zero sau un numar intreg pozitiv.")

    def reverse(self):
        return invers(self.s)

    def extract(self, i, j):
        return self.s[i:j]

    def replace(self, a, b):
        return substituie(self.s, a, b)


s = MyString("0ax1")

print(s ^ 3) 
print(s.reverse())
print(s.extract(1, 3))
print(s.replace("a", "b"))

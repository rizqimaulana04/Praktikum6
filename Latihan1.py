import math
def a(x):
    return x**2
    a = lambda x : x ** 2
print(a(2))
print()

def b(x, y):
    return math.sqrt(x**2 + y**2)
    b = lambda x, y : x ** 2 + y ** 2
print(b(2, 2))
print()

def c(*args):
    return sum(args)/len(args)
    c = lambda *args : sum(args)/len(args)
print(c(5, -6, 7, 8))
print()

def d(s):
    return " ".join(set(s))
    d = lambda s: " ".join(set(s))
print(d("Rizqi"))
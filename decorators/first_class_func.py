def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def calculate(a, b, f):
    return f(a, b)

print(calculate(4, 54, sub))
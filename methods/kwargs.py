def multiply(a, b):
    return a * b
print(multiply(2, 3))

def multiply2(*args):
    res = 1
    for n in args:
        res *= n
    return res

print(multiply2(2, 3, 2))

def multiply3(**kwargs):

    res = 1
    for n in kwargs.values():
        res *= n
    return res

print(multiply3(a=2, b=3, c=2))

def example(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example(a=1, b=2)


def calculate_area(**kwargs):
    print(f"kwargs: {kwargs}")
    if "length" in kwargs and "width" in kwargs:
        # Rectangle area
        return kwargs["length"] * kwargs["width"]
    elif "radius" in kwargs:
        # Circle area
        import math
        return math.pi * kwargs["radius"] ** 2
    else:
        raise ValueError("Provide length and width for rectangle or radius for circle")


print(calculate_area(radius=3))
# print(calculate_area(tool=3))

def pick_evens(*args):
    res = []
    for n in args:
        if n % 2 == 0:
            res.append(n)
    return res

print(pick_evens(1, 2, 3, 4, 5, 6))

def skyline(*args):
    res = 0
    for n in args:
        if n > res:
            res = n
    return res

print(skyline(3, 7, 15, 2, 9))

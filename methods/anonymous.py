def tavan_2(x):
    return x ** 2


a = [3, 4, 2, 8]

for i in range(len(a)):
    a[i] = tavan_2(a[i])

print(a)

tavan_a = map(tavan_2, a)
print(tavan_a)

print(list(tavan_a))

b = [3, 4, 2, 8]

power_b = map(lambda x: x**2, b)

print(list(power_b))


names = ["Alex", "Bob", "Charlie", "David", "Eve", "Frank"]

short_names = filter(lambda s: len(s) <= 3, names)
print(short_names)
print(list(short_names))

# Scopes

def hello():
    name = "Alex"
    print(f"Hello {name}")

name = "John"
print(f"first name is {name}")
hello()
print(f"last name is {name}")


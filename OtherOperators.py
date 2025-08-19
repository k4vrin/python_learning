from random import randint

for i in range(10):
    print(i)

for i in range(6):
    for j in range(6):
        print(i*j, end="\t")
    print()

l = "jadi"
for i in range(len(l)):
    print(i, l[i])

print("Looping through a list:")

for i, j in enumerate(l):
    print(i, j)

names = ["Alex", "Bob", "Charlie"]
sure_names = ["Smith", "Johnson", "Williams"]

for x in zip(names, sure_names):
    print(f"{x[0]} {x[1]}")


if "Alex" in names:
    print("Found Alex!")

print(randint(1, 6))
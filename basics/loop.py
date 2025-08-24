

count = 0
my_list = [1, 2, 3, 4, 5, 'a']
for item in my_list:
    print(item)
    try:
        print(f"Item * 2: {item * 2}")
    except TypeError:
        print("Cannot multiply item by 2")

    if isinstance(item, int):
        if item % 2 == 0:
            print(f"Item is even: {item}")
        else:
            print(f"Item is odd: {item}")
            count += 1
    else:
        print(f"Skipping non-integer item: {item}")

print(f"Total odd items: {count}")



for c in "python":
    print(c)


people = {
    "Alice": (45, "Engineer"),
    "Bob": (30, "Designer"),
    "Charlie": (35, "Teacher"),
    "David": (40, "Manager")
}

for name, (age, profession) in people.items():
    print(f"{name} is {age} years old and works as a {profession}.")

for i in range(1, 4):
    print(i * 2)


words = ["Python", "is", "awesome"]
result = ""

for word in words:
    result += word[0]

print(result)

n = 5
x = 10

for _ in range(n):
    if x % 2 == 0:
        x = (x / 2)
    else:
        x = (x * 2) - 1

print(f"Final value of x: {x}")


print("Looping through numbers 0 to 5:")

a = 0

while a <= 5:
    print(f"Current value of a: {a}")
    a += 1



new_number = 50

while new_number >= 2:
    if new_number % 2 == 0:
        new_number /= 2
    else:
        new_number = (new_number * 3) + 1
    print(f"Current value of new_number: {new_number}")


for i in range(1, 11):
    pass

for j in range(1, 6):
    if j % 2 == 0:
        break
    else:
        print(f"Inner loop iteration: {j}")
        continue
    

print("End of loops.")


nmh = 1

while nmh <= 20:
    if nmh % 3 == 0 and nmh % 5 == 0:
        print(f"value: {nmh} hiphop")
    elif nmh % 3 == 0:
        print(f"value: {nmh} hip")
    elif nmh % 5 == 0:
        print(f"value: {nmh} hop")
    else:
        print(nmh)
    nmh += 1

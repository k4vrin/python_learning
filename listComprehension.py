l = [0, 0.45, 9, -1]

new_l = []
for i in l:
    new_l.append(i * 2)

print(new_l)

new_l2 = [i * 2 for i in l]
print(new_l2)

a = 5

res=""
if a % 2 == 0:
    res = "even"
else:
    res = "odd"

print(f"a is {res}")

res2 = "even" if a % 2 == 0 else "odd"
print(f"a is {res2}")

new_l3 = [i * 2 if i % 2 == 0 else i * 3 for i in l]
print(new_l3)
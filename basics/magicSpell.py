i = int(input("Enter a number: "))

if i % 5 == 0 and i % 3 == 0:
    print("legendery")
elif i % 3 == 0:
    print("magical")
elif i % 5 == 0:
    print("cursed")
else:
    print("normal")



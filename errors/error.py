
try:
    print(a)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


def divis(a, b):
    try:
        return a / b
    except Exception as e:
        print(f"Something went wrong. error: {e}")

print(divis(1, 2))
print(divis(1, 0))


def divide_by_zero_ex(a, b):
    try:
        r = a / b
        pr(r)
    except Exception as e:
        print(f"Something went wrong. error: {e}")
    else:
        print("Nothing went wrong")
    finally:
        print("Finally block")


divide_by_zero_ex(1, 2)
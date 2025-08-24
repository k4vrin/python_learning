import timeit

name = "John"
age = 30

# f-string
time_fstring = timeit.timeit('f"Hello {name}, you are {age} years old."', globals=globals())

# % formatting
time_percent = timeit.timeit('"Hello %s, you are %d years old." % (name, age)', globals=globals())

# .format()
time_format = timeit.timeit('"Hello {}, you are {} years old.".format(name, age)', globals=globals())

print(f"f-string: {time_fstring}")
print(f"% formatting: {time_percent}")
print(f".format(): {time_format}")
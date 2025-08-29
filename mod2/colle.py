import collections

my_list = [1, 2, 3, 4, 5, 1]
c = collections.Counter(my_list)

print(c)
print(c.most_common())
print(c.most_common(2))
print(c.get(2))

Klass = collections.namedtuple(
    "Klass",
    ["students", "avg", "teacher"]
)

science = Klass(students=2, avg=3.0, teacher="Mr. Alex")
print(science)

print(science.students)
print(science.teacher)

a = dict()
a["name"] = "John"
print(a)
print(a["name"])

a2 = collections.defaultdict(lambda: 20)
a2["name"] = "Jale"
print(a2)
print(a2["name"])
print(a2["age"])

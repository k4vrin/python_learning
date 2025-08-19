l = [1, 2, 3]

# help(l.pop)


def hello(name):
    """

    :param name:
    :return:
    """
    print(f"oh hello {name}")

hello("kavrin")
hello("Alex")
hello("John")
hello("Jack")

def sum_of_two_numbers(a, b):
    res = a + b
    return res

res1 = sum_of_two_numbers(1, 5)
print(f"sum of two numbers is {res1}")

def chnda_toosh(s, c):
    """
    Gets a string and a character, and returns
    the number of times that character appears in the string.

    :param s: The input string.
    :param c: The character to count.
    :return: The count of character `c` in string `s`.
    """
    count = 0
    for character in s:
        if character == c:
            count += 1
    return count

print(f"jadidian has {chnda_toosh('jadidian', 'j')} j's in it.")

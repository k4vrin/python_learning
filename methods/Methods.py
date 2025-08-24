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


def tavan(n, t=2):
    javab = 1
    for i in range(t):
        javab *= n
    return javab


print(tavan(5, 0))
print(tavan(5))


def is_even(n):
    """

    :param n:
    :return: True if the provided value is even
    """
    return n % 2 == 0


def number_of_evens(nums):
    count = 0
    for n in nums:
        if is_even(n):
            count += 1
    return count


noe = number_of_evens([1, 2, 3, 6, 10, 17])
print(noe)


def any_even_in_list(nums):
    """

    :param nums:
    :return: True if ANY numbers is even
    """

    for n in nums:
        if is_even(n):
            return True
    return False


def largest(nums):
    largest_n = nums[0]
    for n in nums:
        if n > largest_n:
            largest_n = n
    return largest_n


my_nums = [1, 45, 6, 44, 9, 98]
largest_number = largest(my_nums)
print(largest_number)


def get_odds(nums):
    res = []
    c = 0
    for n in nums:
        if not is_even(n):
            res.append(n)
            c += 1
    return c, res


total_odds, odds = get_odds([1, 2, 3, 4, 5])
print(odds)
print(total_odds)


donations = {
    "jadi": 20,
    "sara": 800,
    "far": 12,
    "hasan" : 9
}


def donations_analysis(donation):
    person = ""
    total = 0
    count = 0
    max_donation = -1
    for name, amount in donation.items():
        total += amount
        count += 1
        if amount > max_donation:
            max_donation = amount
            person = name
    return person, total, count, max_donation


winner, total, count, max_donation = donations_analysis(donations)
print(winner, total, count, max_donation)


donations_analysis(donations)


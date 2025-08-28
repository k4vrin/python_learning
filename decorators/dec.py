from functools import wraps


def run_on_even(func):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            func()
        else:
            print("Hiss")

    return wrapper


@run_on_even
def say_hello():
    print("Hello")

@run_on_even
def say_bye():
    print("Bye")

# run_on_even(say_bye)
# run_on_even(say_hello)


say_hello()
say_bye()


def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hello {name}"

print(greet("Mostafa"))

def shout2(func):
    return lambda *args, **kwargs: func(*args, **kwargs).upper()

@shout2
def greet2(name):
    return f"Hello {name}"

print(greet2("Alex"))
import random


random_num = random.randint(1, 20)

def get_user_guess():
    return int(input("Guess a number between 1 and 20: "))

def is_win(random_num, user_guess):
    return random_num == user_guess

def answer(random_num, user_guess):
    if is_win(random_num, user_guess):
        print("Congrats you won!")
        print(f"The number was {random_num}")
    elif user_guess > random_num:
        print("Too high")
    else:
        print("Too low")



guess = -1
while not is_win(random_num, guess):
    guess = get_user_guess()
    answer(random_num, guess)



age = 2
if age > 18:
    print("Adult")
elif age == 18:
    print("Minor")
else:
    print("Child")


action = "run"
score = 0

if action == "run":
    print("You are running")
    score += 1
elif action == "walk":
    print("You are walking")
    score += 2
else:
    print("You are standing still")

if score > 0:
    print(f"Your score is {score}")

payment = float(input("Enter your payment amount: "))
discount = 0

if payment > 50000:
    discount = 0.2
elif 20000 < payment <= 50000:
    discount = 0.1
else:
    discount = 0

print(f"Your discount is {discount * 100}%")
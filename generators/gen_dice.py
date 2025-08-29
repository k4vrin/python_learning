import random
import pickle


data = []
for i in range(10_000):
    this_one = (random.randint(1, 6), random.randint(1, 6))
    data.append(this_one)

with open("dices.pkl", "wb") as f:
    pickle.dump(data, f)

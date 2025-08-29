import pickle

def get_dice():
    with open("dices.pkl", "rb") as f:
        dices = pickle.load(f)
    for dice in dices:
        yield dice

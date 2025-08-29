from get_dice import get_dice

round = 0

for dice in get_dice():
    print(dice)
    if round > 5:
        break
    else:
        round += 1


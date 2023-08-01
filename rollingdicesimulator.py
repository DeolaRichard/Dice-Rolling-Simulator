import random


def roll_dice():
    roll = input("Roll the dice? (Yes/No): ").lower()

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (Yes/NO): ")

roll_dice()

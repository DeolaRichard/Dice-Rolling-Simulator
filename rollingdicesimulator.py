import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

    roll = input("Roll the dice? (Yes/No): ").lower()  # makes the user input case insensitive

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)  # gets a random integer number within the range 1 to 6 and assigns it dice 1
        dice2 = random.randint(1, 6)  # gets a random integer number within the range 1 to 6 and assigns to dice 2

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))  # joins the dictionary to dice 1
        print("\n".join(dice_drawing[dice2]))  # joins the dictionary to dice 2

        roll = input("Roll again? (Yes/NO): ")  # asks the user to roll again


roll_dice()

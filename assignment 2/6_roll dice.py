import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice():
    rolls = 0
    while True:
        current_roll = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {current_roll}")

        if current_roll == 6:
            print("Congratulations! You rolled a 6.")
            break

    # Bonus roll
    bonus_roll = roll_dice()
    print(f"Bonus Roll: {bonus_roll}")

simulate_dice()

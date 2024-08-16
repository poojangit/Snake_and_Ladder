import random
start_position = 0

def roll_dice():
    return random.randint(1,6)

if __name__ == '__main__':
    print("Welcome to the Snake and ladder game")
    dice_value = roll_dice()
    print(f"The player rolled a {dice_value}")
    
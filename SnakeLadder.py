import random

start_position = 0
end_position = 100


def roll_dice():
    return random.randint(1, 6)


def check_option():
    return random.choice(["no play", "ladder", "snake"])


def snake_ladder_game():
    current_postion = start_position
    count = 0
    print("Welcome to the Snake and ladder game")

    while current_postion < end_position:
        # input("Enter to roll the dice")
        dice_value = roll_dice()
        print(f"The player rolled a {dice_value}")

        random_option = check_option()
        print(f"The player encounterred {random_option}")

        if random_option == "no play":
            print(
                f"NO PLAY : The player will stay at the same position {current_postion} "
            )
        elif random_option == "ladder":
            if (current_postion + dice_value) > 100:
                continue
            count = count + 1
            current_postion += dice_value
            print(
                f"LADDER : The player will move ahead of dice value current postion is {current_postion}"
            )
        elif random_option == "snake":
            if(current_postion - dice_value) < 0 :
                continue
            current_postion -= dice_value
            print(
                f"SNAKE: The player moves behind now current position is {current_postion}"
            )
        if current_postion == end_position :
            print(f"Congratulation you won the excact winning position of: {current_postion}")
            print(f"Number of iteration : {count}")
            break
            
        # print(f"Current postion : {current_postion}")
        print("---------------------------------------")
      
 
if __name__ == "__main__":
    snake_ladder_game()

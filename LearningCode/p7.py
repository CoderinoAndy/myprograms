#Snakes and ladders
player_position = 1
while(True):
    movement_amount = int(input("Movement: "))
    if 2 <= movement_amount <= 12:
        player_position += movement_amount
    elif movement_amount == 0:
        break
    else:
        print("Dude, two die don't make that amount.")
        continue

    if player_position == 9:
        player_position = 34
    elif player_position == 40:
        player_position = 64
    elif player_position == 67:
        player_position = 86
    elif player_position == 54:
        player_position = 19
    elif player_position == 90:
        player_position = 48
    elif player_position == 99:
        player_position = 77

    if player_position > 100:
        print("Haha loser you can't move.")
        player_position -= movement_amount
    elif player_position == 100:
        print("You win!")
        break
    
    print(f"You are at {player_position}!")



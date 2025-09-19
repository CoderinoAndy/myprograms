#Snakes and ladders
player_position = 1

game_dict = {
    9 : 34,
    40 : 64,
    67 : 86,
    54 : 19,
    90 : 48,
    99 : 77,
}
# Key value correlations! Easy access easy life.

while(True):
    movement_amount = int(input("Movement: "))
    if 2 <= movement_amount <= 12:
        player_position += movement_amount
    elif movement_amount == 0:
        break
    else:
        print("Dude, two die don't make that amount.")
        continue
        
    if player_position in game_dict:
        player_position = game_dict[player_position]

    if player_position > 100:
        print("Haha loser you can't move.")
        player_position -= movement_amount
    elif player_position == 100:
        print("You win!")
        break
    
    print(f"You are at {player_position}!")



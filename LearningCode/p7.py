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
# Key value correlations in a dict! Easy access easy life.

while(True):
    movement_amount = int(input("Movement: "))
    if player_position + movement_amount == 100:
        print(f"You are now on square {movement_amount + player_position}!")
        print(f"You Win!")
        break
    else:
        player_position += movement_amount
        if player_position in game_dict:
            player_position = game_dict[player_position]
        elif player_position > 100:
            print("Haha loser you can't move.")
            player_position -= movement_amount
    
    print(f"You are now at {player_position}!")



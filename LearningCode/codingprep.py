from random import randint
counter = 0
random_num = randint(1, 100)

while(True):
    chosen_num = int(input("What is the chosen num? "))

    if chosen_num == random_num:
        counter += 1
        print(f"The number was {random_num}! You guessed it in {counter} moves!")
        break
    elif chosen_num < random_num:
        counter += 1
        print(f"The number you chose was TOO LOW!")
    else:
        counter += 1
        print(f"The number you chose was TOO HIGH!")

# Remember ALL colons
# Remember to int input when taking a number
# Remember to update all variables according to what you want
# Remember to review your code
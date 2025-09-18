#Heads or Tails (Gambling edition)

from random import choice #Choice is a function that randomly chooses from a list

balance = 1000

while True:
    print("welcome to our heads or tails game")

    print(f"Your current balance is ${balance}$")
    wager = int(input("How much do you wager... "))
    if balance - wager < 0:
        print("You don't have that much money!")
        continue
    print(f"You wagered {wager} dollars!!!")
    
    print("Please choose either heads or tails!")
    while True:
        user_input = input("User's choice: ")
        user_input = user_input.lower()
        if user_input in {"heads", "tails", "head", "tail"}: #Checking if the user input is in this "set"
            break
            #Breaking the while loop
        else:
            print("Please enter a valid input!")
    #End of while loop

    randchoice = choice(["heads", "tails"])
    if user_input.lower() in {"heads", "head"} and randchoice == "heads":
        print("Yes, you guessed right!")
        balance += wager
        print(f"New balance: {balance}")
    elif user_input.lower() in {"tails", "tail"} and randchoice == "tails":
        print("Yes, you guessed right!")
        balance += wager
        print(f"New balance: {balance}")
    else:
        print(f"You unfortunately guessed wrong bub, computer chose {randchoice}")
        balance -= wager
        print(f"New balance: {balance}")

    # Play again checker
    playagain = input("Do you want to play again? ")
    playagain = playagain.lower()
    if playagain in {"yes", "yeah", "yuh"}:
        continue
    elif playagain in {"naw", "nah", "no"}:
        break
    else:
        print("uhh, not sure what you meant by that but bye!")
        break
    



#we use AND and OR to combine conditions. Not values!
#immutability, a data type or an object that cannot be mutated
#SETS are immutable!
#Lists, are mutable!
    
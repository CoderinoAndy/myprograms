def FunFairCars(placeInLine, carAmount, carCapacity):
    #Checking if the place in line is covered by the total spaces available on the entire coaster
    if placeInLine <= carAmount*carCapacity:
        #If place in line is less than or equal to the total soaces available on the coaster, the individual may ride
        print("yes")
    else:
        #If not, the user may not ride.
        print("no")

def main():
    while(True):
        try:
            #Taking the place of the individual in the line
            placeInLine = int(input())
            #Taking the amount of cars
            carAmount = int(input())
            #Taking the amount of people a car may hold
            carCapacity = int(input())
            break
        except ValueError:
            print("Please enter a valid integer for each input!")
            continue
    
    FunFairCars(placeInLine, carAmount, carCapacity)

main()
#Strings are alphanumeric and special characters enclosed in quotation marks.
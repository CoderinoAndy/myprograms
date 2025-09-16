def donutshop():
    donuts = int(input("Enter the amount of initial donuts: "))
    eventnumber = int(input("Enter the amount of events: "))
    #Continue doing events until the events are done
    #for x in range(eventnumber):
    #   plusminus = str(input())
    #    donut_magnitude = int(input())
    #    if plusminus == "+":
    #        donuts += donut_magnitude
    #    else:
    #        donuts +- donut_magnitude
    #return donuts
    current_event = 1
    while current_event <= eventnumber and donuts >= 0:
            #moving to the end of the # of events and also ensures the # of donuts is above 0 (no negative donutsu)
            event_type = input("+ or -")
            event_magnitude = int(input("How many donuts associated with the event? "))
            #Taking event type and magnitude from the user
        if event_type == "+":
            donuts += event_magnitude
            #If event type is + we bake (adding donuts)
        else:
            donuts +- event_magnitude
            #If event type is - we sell (selling donuts)
        current_event += 1
        #Move along to the next event
    #end of the while loop
    return donuts
                

print(donutshop())
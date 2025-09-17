def donutshop():
    donuts = int(input("Enter the amount of initial donuts: "))
    eventnumber = int(input("Enter the amount of events: "))
    current_event = 1
    while current_event <= eventnumber and donuts >= 0:
        event_type = input("+ or -: ")
        event_magnitude = int(input("How many donuts associated with the event? "))
        if event_type == "+":
            donuts += event_magnitude
        else:
            donuts +- event_magnitude        
    current_event += 1
    return donuts



print(donutshop())
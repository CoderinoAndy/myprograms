def clean(text):
    clean = ""
    upper = ""
    negative_holder = ""
    positive_holder = ""
    total = 0
    for x in text:
        if x.isalpha() and x.isupper():
            upper += x
            if len(negative_holder) > 1:
                total += int(negative_holder)
                negative_holder = ""
            elif len(positive_holder) > 1:
                total += int(positive_holder)
                positive_holder = ""
        elif x = "-":
            if len(negative_holder) > 0:
                total += int(negative_holder)
                negative_holder += "-"
            else:
                negative_holder += "-"
        elif x.isdigit:
            if len(negative_holder) > 0:
                negative_holder += x
            else:
                positive_holder += x
    clean = upper + str(total)
    return clean
    
    
            
            
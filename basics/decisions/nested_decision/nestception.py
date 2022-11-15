inputs = str(input("Where should I look?\n"))
if (inputs == "in the bedroom"):
    inputs_2 = str(input("Where in the bedroom should I look\n"))
    if (inputs_2 == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif (inputs == "in the bathroom"):
    inputs_2 = str(input("Where in the bathroom should I look?\n"))
    if (inputs_2 == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")    
elif (inputs == "in the lab"):
    inputs_2 = str(input("Where in the lab should I look?\n"))
    if (inputs_2 == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
print("Program Started!")
input_letter = str(input("Please enter a letter:\n"))

if (len(input_letter) == 1):
    asci_letter = ord(input_letter)
    print(f"The ASCII code for {input_letter} is {asci_letter}.")
else:
    print("ERROR. Please input single letter !")
print("Program Ended!")
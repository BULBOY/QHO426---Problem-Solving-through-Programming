print("Program Started!")
print("Please enter an ASCII code:")
ascii_input = int(input())
if (ascii_input in range(32,127)):
    character = chr(ascii_input)
    print(f"The character represented by the ASCII code {abs(ascii_input)} is {character}.")
else:
    print("Sorry,please put the number in correct range!")    

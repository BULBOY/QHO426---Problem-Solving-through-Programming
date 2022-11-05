odd_number = 0
even_number = 0

number_A = int(input("Please enter the first whole number.\n"))
if number_A % 2 == 0:
    even_number += 1
else:
    odd_number +=1           
number_B= int(input("Please enter the second whole number.\n"))
if number_B % 2 == 0:
    even_number += 1
else:
    odd_number +=1        
number_C= int(input("Please enter the third whole number.\n"))
if number_C % 2 == 0:
    even_number += 1
else:
    odd_number += 1

print(f"\nThere were {even_number} even and {odd_number} odd numbers.")


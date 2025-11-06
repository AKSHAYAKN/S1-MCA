from Armstrong import armstrong_number
number = int(input("Enter a number to check if it's an Armstrong number:"))
if armstrong_number(number):
    print(f"{number}is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

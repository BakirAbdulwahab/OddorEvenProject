number = int(input("Which number do you want to check? "))


equation = number % 2

if equation == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
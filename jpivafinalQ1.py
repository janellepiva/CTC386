#Janelle Piva
#Final Q1

name = input("To start, enter your name: ")

print("Menu")
print("__________________")
print("* Option 1")
print("* Option 2")
print("* Option 3")
print("__________________")

choice = int(input("Hello " + name + "! Enter a number to choose an option: "))

if choice == 1:
    print("Why did the computer get cold, " + name + "?")
    print("Because it forgot to close its Windows!")

elif choice == 2:
    food = input("Enter a food: ")
    for i in range(20):
        print(food)

elif choice == 3:
    number = 1
    while number != 0:
        number = int(input("Enter a number (0 to stop): "))
        if number != 0:
            print("Warning: That is not zero. Try again!")

else:
    print("User error. Please restart and choose 1, 2, or 3.")

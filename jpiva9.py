#Janelle
#github text comment

def convert_temp():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print("The temperature in Celsius is:", celsius)

name = input("To start, enter your name: ")

print("Menu")
print("__________________")
print("* Option 1")
print("* Option 2")
print("* Option 3")
print("* Option 4")
print("* Option 5")
print("__________________")

choice = int(input("Hello " + name + "! Enter a number to choose an option: "))

if choice == 1:
    print("How do you make a tissue dance?")
    print("Put a little boogie in it.")

elif choice == 2:
    for i in range(15):
        print(name)

elif choice == 3:
    number = int(input("Enter a number: "))
    for i in range(number):
        print("Not all those who wander are lost. - J. R. R. Tolkein")

elif choice == 4:
    secret = 42
    guess = int(input("What number do you think holds the truth? (0 to 100): "))

    while guess < 0 or guess > 100:
        print("Please enter a number between 0 to 100.")
        guess = int(input("Try your luck (0 to 100): "))

    while guess != secret:
        if guess < secret:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Guess again (0 to 100): "))

        while guess < 0 or guess > 100:
            print("That number is not in the range. Try again.")
            guess = int(input("Guess again (0 to 100): "))

    print("🎉 You unlocked the answer to life, the universe, and everything! You win! 🎉")

elif choice == 5:
    convert_temp()

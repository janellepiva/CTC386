#Janelle Piva:
# Lab 10

def convert_temp():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print("The temperature in Celsius is:", celsius)

def story_game():
    print("Welcome to the Forest of Choices!")
    again = "yes"

    while again == "yes":
        print("You're walking through a mysterious forest and see two paths.")
        print("1: A bright path with flowers")
        print("2: A dark, twisty trail into the shadows")
        path = input("Which path do you take? (1 or 2): ")

        if path == "1":
            print("You follow the bright path and come across a peaceful pond.")
            print("Do you want to:")
            print("1: Sit and rest by the water")
            print("2: Try to catch a magical fish")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                print("You feel relaxed and gain, + 2 to Stamina.")
            elif choice == "2":
                print("The fish grants you one wish, + 1 to Intellgence.")
            else:
                print("A frog jumps on your face, - 1 to Confidence." )

        elif path == "2":
            print("You take the dark path and discover a creepy old cabin.")
            print("Do you want to:")
            print("1: Go inside")
            print("2: Run away")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                print("Inside, a talking cat gives you a riddle, +2 to Wisdom.")
            elif choice == "2":
                print("Your trip over a tree root while escaping, -1 to Agility")
            else:
                print("You freeze in place and a squirrel pelts you with acorns, - 2 to Morale.")

        else:
            print("You wander in circles and drop your trail mix, -1 to Energy.")

        again = input("Do you want to try the forest again? (yes or no): ")

name = input("To start, enter your name: ")

print("Menu")
print("__________________")
print("* Option 1")
print("* Option 2")
print("* Option 3")
print("* Option 4")
print("* Option 5")
print("* Option 6")
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

elif choice == 6:
    story_game()

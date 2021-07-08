import random


def guess_number():
    play = "yes"
    while play.lower() == "yes":

        number = random.randint(1, 101)
        correct = False
        count = 0
        while not correct:
            guess = int(input("Enter a random number between 1 and 100 "))
            if guess == number:
                print("Congratulations, you got the correct number")
                correct = True
            elif guess > number:
                print("Too high")
                print("Try again!")
                correct = False
            elif guess < number:
                print("Too low")
                print("Try again!")
                correct = False

            count += 1
        print("\nyou made", count, "number of guesses")
        play = input("\nType 'yes' to play again: ")


guess_number()

import random

print('')
print("WELCOME TO GUESSING THE NUMBER GAME FROM 1 TO 10")

play_again = 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while play_again == 1:
    computer_guess = random.choice(numbers)
    
    while True:
        try:
            print('')
            user_guess = int(input("Please guess the number from 1 to 10: "))
            if user_guess < 1 or user_guess > 10:
                print('')
                print("Please enter a number from 1 to 10 only")
                continue
            break
        except ValueError:
            print("")
            print("Please enter a numeric value only")
    
    if user_guess != computer_guess:
        print("You guessed the wrong number. The computer's number is", computer_guess)
    else:
        print("Congratulations! You guessed the correct number.")
    
    while True:
        try:
            play_again = int(input('To play again, press 1. To exit, press any number other than 1: '))
            break
        except ValueError:
            print("Please enter only numeric value.")

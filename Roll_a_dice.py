import random

user_sum = 0 
computer_sum = 0
dice_numbers = [1, 2, 3, 4, 5, 6]
continue_game = 1

print("")
print("WELCOME TO A DICE GAME :)")
print("")

while continue_game == 1:
    computer_number = random.choice(dice_numbers)
    computer_sum += computer_number
    
    while True:
        try:
            user_number = int(input("Enter the number you rolled on the dice (1 to 6): "))
            if 1 <= user_number <= 6:
                user_sum += user_number
                break
            else:
                print('Please enter a number from 1 to 6 only')
                continue
        except ValueError:
            print("Please enter a numeric value only")
            continue
    
    while True:
        try:
            continue_game = int(input("To continue playing, press 1. To exit, press any other numeric value: "))
            break
        except ValueError:
            print("Please enter a numeric value only")

else:
    if user_sum > computer_sum:
        print("")
        print("Congratulations! You won the match! Your score is", user_sum, "and the computer's score is", computer_sum)
    elif computer_sum > user_sum:
        print('')
        print("Sorry, the computer won the match! Your score is", user_sum, "and the computer's score is", computer_sum)
    elif user_sum == computer_sum:
        print('')
        print("The match has been drawn! Your score is", user_sum, "and the computer's score is", computer_sum)

import random
print("Welcome to this stone-paper-scissors game!")

options = ["stone", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (stone/paper/scissors/q to quit): ").lower()
    if user_choice == "q":
        print("You have quit the game.")
        break
    if user_choice not in options:
        print("Invalid input. Please enter a valid choice.")
        continue

    random_index = random.randint(0, 2)
    computer_move = options[random_index]
    print("Computer chose", computer_move + ".")

    if user_choice == "stone" and computer_move == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_move == "stone":
        print("You win!")
    elif user_choice == "scissors" and computer_move == "paper":
        print("You win!")
    elif user_choice == computer_move:
        print("It's a draw!")
    else:
        print("You lose!")    

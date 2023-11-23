import random

user_score = 0
computer_score = 0

while True:
    user_input = input("Enter rock, paper, scissors, or quit: ")
    
    # Check if the user input is valid
    if user_input not in ["rock", "paper", "scissors", "quit"]:
        print("Invalid input. Please enter rock, paper, scissors, or quit.")
        continue
    
    # Perform some operations with the user input
    if user_input != "quit":
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        # Determine the winner and update the score
        if user_input == computer_choice:
            print("It's a tie!")
        elif (user_input == "rock" and computer_choice == "scissors") or (user_input == "scissors" and computer_choice == "paper") or (user_input == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    
    # Break the loop if the user wants to quit
    if user_input == "quit":
        print("User Score:", user_score)
        print("Computer Score:", computer_score)
        if user_score > computer_score:
            print("User wins!")
        elif user_score < computer_score:
            print("Computer wins!")
        else:
            print("It's a tie!")
        break


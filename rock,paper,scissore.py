import random

# The function below get the choice that the computer make using random number
def get_computer_choice():
    # Generate random between 0-2, and 0-2 each corresponding to: 
    #0:Rock, 1 : Paper, 2 : Scissors.
    choice=random.randint(0, 2)

    if choice == 0:
        return 'R'  # Rock
    elif choice == 1:
        return 'P'  # Paper
    else:
        return 'S'  # Scissors

# Function to decide the winner by using if
def determine_winner(player_choice, computer_choice):
    # If both choices are the same then it's a tie
    if player_choice == computer_choice:
        return "It's a tie!"
    
 # Check if player wins with the following conditions
    elif player_choice == 'R' and computer_choice == 'S':
        return "You win!"
    elif player_choice == 'P' and computer_choice == 'R':
        return "You win!"
    elif player_choice == 'S' and computer_choice == 'P':
        return "You win!"
    
    #If none of the above, Player lost
    else:
        return "You lose!"

# Principal function running the game
def play_game():
   # Get the player's choice (expecting 'R', 'P', or 'S')
    player_choice = input("Enter R for rock, P for paper, or S for scissors: ").upper()

    # Check if the player's input is valid
    if player_choice not in ['R', 'P', 'S']:
        print("Invalid choice. Please choose R, P, or S.")
    return  # If input is invalid

    # Computer's choice determination
    computer_choice = get_computer_choice()
    print(f"Computer chooses: {computer_choice}")

    # Choose winner and reveal the outcome.
    result = determine_winner(player_choice, computer_choice)
    print(result)

# To make call of this module play this game.
    play_game()

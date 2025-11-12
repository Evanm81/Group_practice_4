print("Welcome to Rock-Paper-Scissors!")
def get_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please choose 'Rock', 'Paper', or 'Scissors'.")
player_choice = get_user_choice()
print(f"You chose: {player_choice}")
import random

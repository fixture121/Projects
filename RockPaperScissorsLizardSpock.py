import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("\nEnter rock, paper, scissors, lizard, or spock (or enter 'rules' to see rules): ").lower()
        if user_input == "rules":
            display_rules()
        elif user_input in ["rock", "paper", "scissors", "lizard", "spock"]:
            return user_input
        else:
            print("Invalid choice. Please try again.")

def display_rules():
    print("""
          Rules of Rock, Paper, Scissors, Lizard, Spock:
          - Rock crushes Scissors
          - Scissors cuts Paper
          - Paper covers Rock
          - Rock crushes Lizard
          - Lizard poisons Spock
          - Spock smashes Scissors
          - Scissors decpitates Lizard
          - Lizard eats Paper
          - Paper disproves Spock
          - Spock vaporizes Rock
          """)

def determine_winner(user_choice, computer_choice):
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if user_choice == computer_choice:
        return "tie"
    elif computer_choice in winning_combinations[user_choice]:
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0

    print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1

        print(f"Score: You {user_wins} - {computer_wins} Computer")

        play_again = input("\nDo you want to play again? (Enter 'y' to play again or any key to quit game): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()

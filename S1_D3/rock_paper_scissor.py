import random

choices = ["rock", "paper", "scissors"]
scores = {
    "user": 0,
    "computer": 0,
    "draws": 0
}

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if choice == "q":
            return None
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def print_scores():
    print(f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draws']}")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print_scores()
        user_choice = get_user_choice()
        if user_choice is None:
            break
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            scores["user"] += 1
            print("You win!")
        elif winner == "computer":
            scores["computer"] += 1
            print("Computer wins!")
        else:
            scores["draws"] += 1
            print("It's a draw!")
        print()

play_game()
print("Thanks for playing!")

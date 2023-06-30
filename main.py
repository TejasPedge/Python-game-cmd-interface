import random

def get_user_choice():
    while True:
        print("Enter your choice: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        choice = input("Your choice (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 4:
                return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

def display_result(user_choice, computer_choice, winner):
    print("User chose:", user_choice)
    print("Computer chose:", computer_choice)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

def update_scores(scores, winner):
    if winner == "User":
        scores["User"] += 1
    elif winner == "Computer":
        scores["Computer"] += 1
    else:
        scores["Draws"] += 1

def display_scores(scores):
    print("----- Scores -----")
    print(f"User: {scores['User']}")
    print(f"Computer: {scores['Computer']}")
    print(f"Draws: {scores['Draws']}")
    print("------------------")

def play_game():
    scores = {"User": 0, "Computer": 0, "Draws": 0}

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        user_choice = get_user_choice()

        if user_choice == 4:
            print("Thanks for playing!")
            break

        user_choice = ["Rock", "Paper", "Scissors"][user_choice - 1]
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        update_scores(scores, winner)

        display_scores(scores)
        print()

play_game()

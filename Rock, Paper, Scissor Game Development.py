import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter either rock, paper, or scissors.")

def get_computer_choice(user_choice):
    choices = ['rock', 'paper', 'scissors']
    choices.remove(user_choice)
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice(user_choice)
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

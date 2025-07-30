import random

options = ['rock', 'paper', 'scissors']
user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in options:
    print('Invalid Input!')
else:
    computer_choice = random.choice(options)
    print(f"\nYou chose: {user_choice}")
    print(f"computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
         (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You Win!")
    else:
        print("Computer wins!")
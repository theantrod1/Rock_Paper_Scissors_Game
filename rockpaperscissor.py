import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0-2]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Type valid answer.")
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print(f"Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("It's a tie!")
        continue
    else:
        print("You lose!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye")

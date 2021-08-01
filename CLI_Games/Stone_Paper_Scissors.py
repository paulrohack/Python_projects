import random

options = ["STONE", "PAPER", "SCISSORS"]
win = 0
lose = 0
n = 5
for _ in range(n):
    i = random.randint(0, len(options)-1)
    computer_choice = options[i]

    # print(computer_choice)
    user_input = input("Choose :").upper()
    if user_input not in options:
        print("Not in the Options\nStone, Paper, Scissors\n")
    elif computer_choice == user_input:
        print("..DRAW..\n")
    elif computer_choice == "PAPER" and user_input == "STONE":
        lose += 1
        print(f"COMPUTER CHOICE WAS {computer_choice}")
        print("..COMPUTER WIN..\n")
    elif computer_choice == "SCISSORS" and user_input == "PAPER":
        lose += 1
        print(f"COMPUTER CHOICE WAS {computer_choice}")
        print("..COMPUTER WIN..\n")
    elif computer_choice == "STONE" and user_input == "SCISSORS":
        lose += 1
        print(f"COMPUTER CHOICE WAS {computer_choice}")
        print("..COMPUTER WIN..\n")
    else:
        win += 1
        print(f"COMPUTER CHOICE WAS {computer_choice}")
        print("..YOU WIN..\n")



print(f"COMPUTER WON {lose} TIMES.\nYOU WON {win} TIMES.\nDRAW BETWEEN BOTH {n - (win + lose)} TIMES")
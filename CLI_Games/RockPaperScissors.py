import random, os

random.seed(random.randint(1, 10))
OPTIONS = ["R", "S", "P"]
d = {"R": "ROCK", "S": "SCISSORS", "P" : "PAPER"}

WIN = 0
LOSE = 0
n = 5
os.system('cls')
for _ in range(5):
    CC = d[random.choice(OPTIONS)]
    USER_INPUT = input("Choose [R]ock [P]aper [S]cissors :").upper()
    CHOICE = d[USER_INPUT]
    if USER_INPUT not in OPTIONS:
        print("Not in the Options\n[R]ock, [P]aper, [S]cissors\n")
    elif CC == CHOICE:
        print("..DRAW..\n")
    elif CC == "PAPER" and CHOICE == "STONE":
        LOSE += 1
        print(f"COMPUTER CHOICE WAS {CC}")
        print("..COMPUTER WIN..\n")
    elif CC == "SCISSORS" and CHOICE == "PAPER":
        LOSE += 1
        print(f"COMPUTER CHOICE WAS {CC}")
        print("..COMPUTER WIN..\n")
    elif CC == "STONE" and CHOICE == "SCISSORS":
        LOSE += 1
        print(f"COMPUTER CHOICE WAS {CC}")
        print("..COMPUTER WIN..\n")
    else:
        WIN += 1
        print(f"COMPUTER CHOICE WAS {CC}")
        print("..YOU WIN..\n")
print(f"COMPUTER WON {LOSE} TIMES.\nYOU WON {WIN} TIMES.")
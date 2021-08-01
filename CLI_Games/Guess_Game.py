import math,random, os
digits = "1234567890"
Num_guess = ""
for i in range (2):
    Num_guess += digits[math.floor(random.random() * 9)]
mx = 100
mn = 10
os.system('cls')
print(f"Guess a number b/w {mn} - {mx}")
guess = 1
def main():
    global guess
    ask = input(("guess a number :"))
    if ask == Num_guess:
        print("Your guess was right")
        print("CONGRATULATIONS :)")
        if guess < 7:
            print("WINNER!WINNER!CHICKEN DINNER")
        else:
            print("Great Job! But try for CHICKEN DINNER")
        print(f"you used {guess} guess to guess this number" )
        quit()               
    elif ask < Num_guess:
        print("Your guess was small")
        guess += 1
    elif ask > Num_guess:
        print("Your guess was  big")
        guess += 1
    if ask == "q":
        os.system('cls')
        print("You have quitted!")
        print(f"The number is {Num_guess}" )
        quit() 
while True:
    main()


        
        



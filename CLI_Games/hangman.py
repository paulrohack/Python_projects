import random, os
path = 'CLI_Games'
os.system('cls')
def spacedOut(word, guessed=[]):
    lenght = len(word)
    spacedWord = ' '
    guessedLetters = guessed
    for x in range(lenght-1):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
Wrong_guess = [0,1,2,3,4,5,6,7]
Wrong_guess[0] =(''' 
                      +---+
                      |   |
                          |
                          |
                          |
                          |
                     =========''')
Wrong_guess[1] =(''' 
                      +---+
                      |   |
                      0   |
                          |
                          |
                          |
                     =========''')
Wrong_guess[2] =(''' 
                      +---+
                      |   |
                      0   |
                      |   |
                      |   |
                          |
                     =========''')
Wrong_guess[3] =(''' 
                      +---+
                      |   |
                      0   |
                     /|   |
                      |   |
                          |
                     =========''')
Wrong_guess[4] =('''
                     +---+
                      |   |
                      0   |
                     /|\  |
                      |   |
                          |
                     =========''')
Wrong_guess[5] =(''' 
                       +---+
                      |   |
                      0   |
                     /|\  |
                      |   |
                     /    |
                     =========''')
Wrong_guess[6] =(''' 
                       +---+
                      |   |
                      0   |
                     /|\  |
                      |   |
                     / \  |
                     =========''')
Wrong_guess[7] =('''
                   RIP RIP             
                   RIP RIP
                   RIP RIP
                   RIP RIP
                   RIP RIP
                                       
                  ''')
 #################################
#   Actual game play starts here   #
 ##################################
txt = open('CLI_Games\easy_words.txt')
words = txt.readlines()
listWORDS = (words[random.randrange(0,len(words))])
word =(listWORDS).upper()
gamePlay = True
guessed = []
wrongGuessed = []
guess = 0
right_guess = 0
i = 0
num = len(word)
print("IM HANGMAN \nPLEASE SAVE ME BY GUESSING THE WORD \nIF NOT I'LL DIE")
print(F"ITS A {num - 1} DIGIT WORD")
while gamePlay:
    ask = input(">>>    ").upper()
    if len(ask) > 1:
        print("GUESS ONE ALPHABET")
    elif len(ask) == 0:
        print('NO GUESS')
    elif guess == 7 :
        print(Wrong_guess[7])
        print('LOST!')
        print(f'THE WORD IS {word.upper()}')
        quit()
    elif ask in guessed or ask in wrongGuessed:
        print("ALREADY GUESSED")
    else:
        if ask in word:
            print('RIGHT')
            guessed.append(str(ask))
            print(spacedOut(word,guessed))
            if spacedOut(word, guessed).count('_ ') == 0:
                print("WON!")
                quit()
        else:
            wrongGuessed.append(str(ask))
            print(Wrong_guess[i])
            i = i + 1
            print('WRONG')
            print(spacedOut(word,guessed))
            guess = guess + 1

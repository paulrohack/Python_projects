import time, os
from random import choice
from matplotlib import pyplot as p

words = []
graph = {}
with open("CLI_Games\easy_words.txt", 'r') as f:
    w = f.readlines()
for i in (w):
    words.append(i.replace('\n', '').lower())
def mean(n):
    total_sum = sum(n)
    total_nos = len(n)
    if total_nos == 0: total_nos = 0.1
    return round((total_sum/total_nos), 2)
time_taken = []
os.system('cls')
turns = int(input("How may Turns Would you want to try [recommended: 15 or 30 or 60]:  "))
if turns < 10:
    print("Number of words are taken as 10, because of the very less word limit!")
    turns = 5

words_made_wrong = {}
e = 0
print("When your ready hit ENTER!")
if input() == "":
    print(" ")
    os.system('cls')
    while e < turns:
        word_given = choice(words)
        start = time.time()
        word =  input(f"{e + 1}) {word_given} : ").lower().split()
        end = time.time()
        Time = end-start
        if word == [] :
            e -= 1
        elif word[0] != word_given:
            words_made_wrong[e] = (word_given)
        else:
            time_taken.append(Time)            
        e += 1
        graph[e] = round(Time, 2)
    if len(words_made_wrong) > turns - 2 or mean(time_taken) == 0.0:
        print("You better take this test Serious!")
    else:
        print("WPS: ", mean(time_taken), f" ==> That means you took Average of {mean(time_taken)} seconds.")    
        print("Words that need More Practice", list(words_made_wrong.values()))
        gx = list(graph.keys())
        gy = list(graph.values())
        p.bar(range(len(graph)), gy, tick_label=gx)
        p.plot(range(len(graph)), gy, color="pink", markersize=10)
        p.plot(range(len(words)), list(words_made_wrong.keys()), 'o', color="red", markersize=20)


        p.show()



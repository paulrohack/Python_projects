import time
from random import choice
import os

words = ['about','act','actually','add','name','after','again','against','age','ago','air','all','also','always','among','another','answer','appear','are','area','as','ask','at',
'you','back','ball','base','be','beauty','because','become','bed','been','before','began','begin','behind','best','better','between','big','bird','black','blue','boat',
'body','book','both','bottom','box','boy','bring','brought','build','built','busy','call','came','can','car','care','carefully','carry','centre','certain','change',
'check','child','children','city','class','clear','close','cold','colour','come','common','community','complete','contain','could','country','course','create','cried',
'cross','cry','cut']

def mean(n):
    total_sum = sum(n)
    total_nos = len(n)
    return round((total_sum/total_nos), 2)
time_taken = []
turns = int(input("How may Turns Would you want to try [recommended: 15 or 30 or 60]:  "))
if turns < 10:
    print("Number of words are taken as 10, because of the very less word limit!")
    turns = 10

words_made_wrong = []
os.system('cls')
print("When your ready hit ENTER!")
if input() == "":
    for i in range(turns):
        word_given = choice(words)
        print(word_given)
        start = time.time()
        word =  input().lower().split()
        end = time.time()
        Time = end-start
        if word[0] != word_given:
            words_made_wrong.append(word_given)
        else:
            time_taken.append(Time)
        os.system('cls')
    print("WPS >>", mean(time_taken), f"\nThat means you took Average of {mean(time_taken)} seconds.")
    print("Words that need More Practice", words_made_wrong)
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
            print("Wrong Word")
        else:
            time_taken.append(Time)
        os.system('cls')
    print("Word Per Second", mean(time_taken))
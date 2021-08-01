import random

truth_list = ["Who is your favorite teacher?"
"What is a word that you’ve made up?",
"What is your favorite meal Mom makes?",
"Have you ever lied about your age?",
'Would you rather have a pet or a sibling?',
"What was the biggest joke you’ve ever played on someone?",
"Do you have a unique talent?",
"Do you sing in the shower?",
"Who would win in a fight- Hulk or Iron Man?",
"Have you ever peed the bed?",
"What one thing are you always losing track of?",
"How do you cheat on a chore?",
"When was the last time you were bored out of your brains?"
"How often do you floss your teeth?",
"Which celebrity would you be, and why?",
"Are you a dog person or a cat person?",
"Are you afraid of ghosts?",
"Which are the funniest words you know?",
"Have you poured a glass of milk on a plant?",
"Have you ever broken something and not told anyone?",
"Have you ever cried during a movie?",
"Do you apologize after an argument?",
"If you had 1 minute to get out of your house, what would you grab?",
"Do you think rain smells good?",
"If you had a pet dinosaur, which would you pick?"]

dare_list = ["Give someone a piggyback ride"
"Do not blink for a minute",
"Any time someone takes a drink, ask them for a sip",
"Do your best Buzz Lightyear impression",
"Run around the outside of the house three times",
"Go outside and yell “I pick my nose” to the first person you see",
"Put your leg behind your head",
"Eat a spoonful of hot sauce",
"Hug your mailbox (or a tree or lawn ornament) for 20 seconds",
"Sing the Star-Spangled Banner in your best opera voice",
"Take a bite out of a stick of butter",
"Draw a face on your hand and talk with your hand when it’s your turn",
"Let the person standing closest to you do your make-up crazy. Keep it on for at least an hour",
"Talk with your tongue sticking out",
"Do the next dare for the next person that gets one",
"Text someone using only your nose",
"Use the driveway as a catwalk for 5 minutes and wave to passing people",
"Brush your teeth in front of everyone",
"Do jumping jacks until your next turn",
"Do 10 perfect pushups",
"Go up to anyone on the street and ask “how could you?” with much emotion",
"Eat a spoonful of mustard",
"Play the air guitar"]

while True:
    user = input(">>> ").upper()
    if user == 'TRUTH':
        print(random.choice(truth_list))
    elif user == 'DARE':
        print(random.choice(dare_list))
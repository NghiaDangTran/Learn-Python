# this will make a simple rock paper scissor game

import random

choices = ["rock", "paper", "scissor"]
comp = random.choice(choices)

user = None




while True:
    while user != "1" or user != "2" or user != "3":
        user = input("Pls pick 1 to 3 (rock, paper, scissors)\n")
        if user == "" or user == "break" or user=="quit" or user == "1" or user == "2" or user == "3":
            break

    if (user == "1" or user == "2" or user == "3"):
        user=int(user)
        user_input = choices[user-1]
        
        if (
        (comp == choices[0] and user_input == choices[1])
        or (comp == choices[1] and user_input == choices[2])
        or (comp == choices[2] and user_input == choices[0])
        ):
            print("User win")
        elif comp==user_input:
            print("Draw")
        else:
            print("comp win")
    next=input("Do you still want to play? (Yes or No)\n")
   
    if next=="No": 
        print("the game Ended") 
        break

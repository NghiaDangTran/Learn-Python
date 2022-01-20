import image,re
import words_data
import random


def words_generator():
    return random.choice(words_data.words)
def find_word(tofind,char):
    result=[]
    for i in range(len(tofind)):
        if(tofind[i]==char):
            result.append(i)
    print (result)
find_word(list("asdasd"),"1")









def process(solution,currentGuess,GameFase):
    currentGuess=""
    guess=list(map(lambda x: "_", list(solution)))
    while GameFase>=0:
        display_curr_state(GameFase)
        display_guess()
        while True:
            input_str = raw_input("Please enter your guess(1 word only)\n")
            if not re.match("^[a-z]*$", input_str):
                print "Error! Only letters a-z allowed!"
                continue
            elif len(input_str) != 1:
                print "Error! only 1 word pls"
                continue
            else:
                break
        if(input_str in currentGuess):
            print(" you areealdy guess3ed it ")
            continue
        if(input_str in solution):
            
            fill=find_word(solution)
            print("Great there are ",len(fill),"words in the string")
            for i in range(len(fill)):
                guess[i]=input_str
            continue
        
            GameFase+=1
            




# solution="words_generator()"
# chjeck=['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
# data=list(map(lambda x: "_", list(solution)))
# print(str(data))


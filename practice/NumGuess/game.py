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
    return result






def display_curr_state(GameFase):
    print(image.Hang[GameFase])



def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))



def process(solution,GameFase):
    guess=list(map(lambda x: "_", list(solution)))
    while GameFase>=0:
        
       
        display_curr_state(GameFase)
        print(guess)
        
        result=listToString(guess) 
       
        if(result==solution):
           break
        while True:
            input_str = input("Please enter your guess(1 word only)\n")
            if not re.match("^[a-z]*$", input_str):
                print( "Error! Only letters a-z allowed!")
                continue
            elif len(input_str) != 1:
                print ("Error! only 1 word pls")
                continue
            else:
                break
        if(input_str in guess):
            print(" you areealdy guess3ed it ")
            continue
        elif(input_str in solution):
            
            fill=find_word(list(solution),(input_str))
            print(len(fill))
            print("Great there are ",len(fill),"words in the string")
            for i in range(len(fill)):
                guess[fill[i]]=input_str
            continue
        print("unfortunate there is no word u guessed in the string")
        GameFase-=1
    if(GameFase==-1):
        print(": you lost")
    else: print("you won")
            
process(words_generator(),8)



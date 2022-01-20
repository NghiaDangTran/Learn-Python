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
find_word("asdasd","a")









def process(solution,currentGuess,GameFase):
    currentGuess=""
    guess=list(map(lambda x: "_", list(solution)))
    while GameFase>=0:
        while True:
            input_str = raw_input("Please enter your guess(1 word only)\n")
            if not re.match("^[a-z]*$", input_str):
                print "Error! Only letters a-z allowed!"
                pass
            elif len(input_str) != 1:
                print "Error! only 1 word pls"
                pass
            else:
                break
        if()






solution="words_generator()"
chjeck=['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
data=list(map(lambda x: "_", list(solution)))
print(str(data))


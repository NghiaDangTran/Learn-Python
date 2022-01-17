import os
import os.path
import shutil
user_ans = []
solution = []


def process_data(data_file):
    print("tes")
    count = 0
    question = ""

    with open(data_file) as fp:
        while True:

            line = fp.readline()

            if not line:
                break
            if "Question" in line:
                count += 1
                question = ""
                print("\nthis is the question " + str(count))
            elif "#*#*#answer#*#*#" in line:
                print(question)
                user_ans.append(input("What is your answer? \n").lower())
                solution.append(line[0:-18].lower())
                question = ""

            else:
                question += line

d = os.getcwd()

process_data(d+"/practice/QuizGame/data.txt")
print(user_ans)
print(solution)

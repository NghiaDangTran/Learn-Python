import random
from random import randint
class Board:
    def gencoordinates(self,m, n,max):
        seen = []

    

        total=0
        while(total<max):
            x= randint(m, n)
            y=randint(m, n)
            tupple=(x,y)
            if(tupple not in seen):
                seen.append(tupple)
                total+=1

        return seen
    def __init__(self,size,boom):
        self.size=size
        self.boom=boom
        self.bom_location=self.gencoordinates(0,size-1,boom)

        self.playerLocation=[]
        self.board=[ [ "_" for i in range(size) ] for j in range(size) ]
        self.end=False



    def print(self):
       result=""
       for i in range(self.size):
           for j in range(self.size):
               
               result+="|"+self.board[i][j]
           result+="|\n"
       print(result)
       


    def playerMove(self):
        x=int(input("pls enter the row u want to play(from 1 to size the board)"))
        y=int(input("pls enter the col u want to play(from 1 to size the board)"))
        if x<1 or x>self.size or y<1 or y>self.size :
            print("your input is wrong")
            return False
        toadd=(int(x)-1,int(y)-1)
        if(toadd in self.bom_location):
            self.end=True
            print("yessssssssssssssssssssss")
        if(toadd not in self.playerLocation):
            self.playerLocation.append(toadd)
            if(len(self.playerLocation)==self.size*self.size):
                self.end=True
            self.board[x-1][y-1]="X"
            return True
        else: 
            print("the location already move")
            return False
    

def game_star():
    board_size=int(input("pls enter the board size\n"))
    game=Board(board_size,randint(board_size,board_size*2))
    while(True):
        check=False
        while(check==False):
            check=game.playerMove()
        print(game.bom_location)
        if(game.end==True):
            print("YOU LOSS SO BAD")
            break
        game.print()



       
    

game_star()

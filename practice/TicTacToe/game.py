import random
from player import HumanPlayer ,Noob_comp
from SO_YOU_WANT_TO_CHOSE_HARD_MODE import HARD_MODE

class TicTacToe:
    def __init__(self,row,col):
        self.player1=""
        self.player2=""
        self.col=col
        self.row=row
        self.board=[ [ "_" for i in range(row) ] for j in range(col) ]
        # self.board=[["_"]*col]*row
        self.current_winner=None
    def print_board(self):
        result=""
        for i in range(self.col):
            for j in range(self.row):
                
                result+="|"+self.board[i][j]
            result+="|\n"
        print(result)

    def move_ok(self):
        result=[]
        for i in range(self.col):
           for j in range(self.row):
               
               if(self.board[i][j]=="_"):
                   result.append((i,j))
           
        return result
   
    def fill_postion(self,atrow,atcol,value,printOK=True):
        if(self.current_winner!=None):
            print("there already a winner pls make new game")
            return 
        if len(self.move_ok())==0:
            print("NO more place to move")
            return
      
        if(self.board[atrow][atcol]=="_" ):
            self.board[atrow][atcol]=value
        else : print("there is a value here\n")
        checkR=checkC=diag=rdiag=0
        for i in range(self.col):
            if self.board[atrow][i]==value:
                checkR+=1
            if self.board[i][atcol]==value:
                checkC+=1
            if self.board[i][i]==value:
                diag+=1
           
            if self.board[i][self.col-1-i]==value:
                rdiag+=1
        if checkC==self.col or checkR==self.col or diag==self.col or rdiag==self.col:
            self.current_winner= value
        if(self.current_winner!=None and printOK):
            print("player",format(self.current_winner),"won")

            return
        if len(self.move_ok())==0 and printOK:
            print("The game is TIe no one win")
            return

            

    def check_winner(self):
        return self.check_winner
    # def num_empty_squares(self):
    #     result=0
    #     for i in range(self.col):
    #        for j in range(self.row):
               
    #            if(self.board[i][j]=="_"):
    #                result+=1
           
    #     return result   

def start(TicTacToe,Xplayer,Oplayer):
    newGamne=random.randint(1, 10)
    newPlayer=""
    if newGamne<5: newPlayer="X" 
    else: newPlayer="O"

    while len(TicTacToe.move_ok())!=0:
        if newPlayer=="O": Move = Oplayer.get_move(TicTacToe)
        else: Move = Xplayer.get_move(TicTacToe)
        TicTacToe.fill_postion(Move[0],Move[1],newPlayer)
        TicTacToe.print_board()
        

        if(TicTacToe.current_winner!=None):
            break
        if(newPlayer=="O"): newPlayer="X"
        else: newPlayer="O"


    
# board=TicTacToe(3,3)
# board.fill_postion(0,0,"X")
# board.fill_postion(0,1,"O")
# board.fill_postion(0,2,"X")
# board.fill_postion(1,1,"O")
# board.fill_postion(2,1,"X")
# board.fill_postion(1,0,"O")
# board.fill_postion(2,0,"X")
# board.fill_postion(1,2,"O")



# board.print_board()
       




if __name__ == '__main__':
    # x_player = HARD_MODE('X',5)
    # o_player = HARD_MODE('O',5)
    t = TicTacToe(3 ,3)
    t.print_board()
    t.board
        # start(t, x_player, o_player)

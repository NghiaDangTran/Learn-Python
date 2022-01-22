import random
class HumanPlayer():
    def __init__(self, letter):
        self.symbol=(letter)

    def get_move(self, game):
        valid_square = False
        val = None
      
        print("avalabe move:")
        print(game.move_ok())
        square = input(self.symbol + '\'s turn. Input from the above list: ')
        val = game.move_ok()[int(square)]
            # try:
            #     val = game.move_ok[int(square)]
            #     if val not in game.move_ok():
            #         raise ValueError
            #     valid_square = True
            # except ValueError:
            #     print('Invalid square. Try again.')
        return val
class Noob_comp():
    def __init__(self, letter):
        self.symbol=(letter)

    def get_move(self, game):
        valid_square = False
        val = None
      
        print("avalabe move:")
        print(game.move_ok())
        square = random.randint(0,len(game.move_ok())-1)
        val = game.move_ok()[int(square)]
            # try:
            #     val = game.move_ok[int(square)]
            #     if val not in game.move_ok():
            #         raise ValueError
            #     valid_square = True
            # except ValueError:
            #     print('Invalid square. Try again.')
        return val
import random
import math

class HARD_MODE():
    def __init__(self, letter,size):
      self.letter=(letter)
      self.size=size

    def get_move(self, game):
        if len(game.move_ok()) >= (self.size*self.size)/2:
            square = random.choice(game.move_ok())
        else:
            
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
        # first we want to check if the previous move is a winner
        if game.current_winner == other_player:
            return {'position': None, 'score': 1 * (len(game.move_ok()) + 1) if other_player == max_player else -1 * (
                        len(game.move_ok()) + 1)}
        elif len(game.move_ok())==0:
            return {'position': None, 'score': 0}
      
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in game.move_ok():
            game.fill_postion(possible_move[0],possible_move[1], player,False)
            sim_score = self.minimax(game, other_player)  # simulate a game after making that move
            # undo move
            
            game.board[possible_move[0]][possible_move[1]] = '_'
            game.current_winner = None
            # if sim_score['score']==0:
            sim_score['position'] = possible_move  # this represents the move optimal next move
            print(sim_score)
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
            # print(best)
        return best


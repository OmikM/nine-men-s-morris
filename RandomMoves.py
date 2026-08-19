import random

class RandomMoves:
    def __init__(self, player_num :int):
        self.last_board = [[]]
        self.moves_left = []
        self.player_num = player_num

    def helper(self, board):
        if(self.last_board != board.board):
            self.last_board = board.board
            self.moves_left = list(range(25))
            random.shuffle(self.moves_left)

        move = self.moves_left[0]
        self.moves_left.pop(0)
        return move

    def place_pawn(self,board):
        return random.choice(board.get_possible_moves_place())
    
    def delete_pawn(self, board, whose):
        return random.choice(board.get_possible_moves_delete(whose))
    
    def move_pawn(self,board):
        board.print_board()
        temp = board.get_possible_moves_move(self.player_num)
        return random.choice(temp)
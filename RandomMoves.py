import random

class RandomMoves:
    def __init__(self):
        self.last_board = [[]]
        self.moves_left = []

    def helper(self, board):
        if(self.last_board != board.board):
            self.last_board = board.board
            self.moves_left = list(range(25))
            random.shuffle(self.moves_left)

        move = self.moves_left[0]
        self.moves_left.pop(0)
        return move

    def place_pawn(self,board):
        return self.helper(board)
    def delete_pawn(self, board):
        return self.helper(board)
    def move_pawn(self,board):
        return random.randint(0,23), random.randint(0,23)
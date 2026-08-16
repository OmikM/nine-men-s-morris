from board import Board
class Person:
    def __init__(self):
        pass
    def place_pawn(self,board):
        board.print_board()
        return int(input("where do you want to place pawn? "))
    def delete_pawn(self, board):
        board.print_board()
        return int(input("witch opponent's pawn do you want to delete? "))
    def move_pawn(self,board):
            return self.helper(),self.helper()

        
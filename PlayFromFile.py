
class PlayFromFile:
    def __init__(self, file):
        self.file = file
        self.moves = []
        with open(file, "r") as f:
            for l in f.read().split():
                self.moves.append(int(l))
                

    def helper(self):
        m = self.moves[0]
        self.moves.pop(0)
        input()
        return m

    def place_pawn(self,board):
        return self.helper()
    def delete_pawn(self, board,whose):
        return self.helper()
    def move_pawn(self,board):
        return self.helper(),self.helper()

        
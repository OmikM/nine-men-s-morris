from board import Board
class Game:
    def __init__(self,player_1, player_2):
        self.pawns_1_free = 9
        self.pawns_1_onboard = 0
        self.pawns_2_free = 9
        self.pawns_2_onboard = 0
        # turn 1 - player 1 to move 
        self.whose_turn = 1

        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()

    def place_pawn(self):
        if(self.whose_turn == 1):
            move = self.player_1.place_pawn(self.board)
        else:
            move = self.player_2.place_pawn(self.board)

        if (move not in self.board.get_possible_moves_place()):
            return self.place_pawn()


        self.board.board[move] = self.whose_turn

        if self.whose_turn == 1:
            self.pawns_1_free-=1
            self.pawns_1_onboard+=1
        else:
            self.pawns_2_free-=1
            self.pawns_2_onboard+=1
        print(move)
        return move
    
    # whose pawn should be removed
    def delete_pawn(self, whose):
        if(self.whose_turn == 1):
            move = self.player_1.delete_pawn(self.board,whose)
        else:
            move = self.player_2.delete_pawn(self.board,whose)

        if(move not in self.board.get_possible_moves_delete(whose)):
            return self.delete_pawn(whose)

        print(move)
        
        self.board.board[move] = 0
        
        if self.whose_turn == 1:
            self.pawns_2_onboard-=1
        else:
            self.pawns_1_onboard-=1
        
        return move

    def move_pawn(self):
        if (self.whose_turn == 1):
            From, To = self.player_1.move_pawn(self.board)
        else:
            From, To = self.player_2.move_pawn(self.board)

        if([From, To] not in self.board.get_possible_moves_move(self.whose_turn)):
            return self.move_pawn()
        
        print(From)
        print(To)
        self.board.board[From] = 0
        self.board.board[To] = self.whose_turn

        return To

    


    def is_new_mill(self, tile, ax = 0):
        

        mill = self.board.get_mill(ax, tile)
        if(mill[0]*mill[1]*mill[2] == 1 or mill[0]*mill[1]*mill[2] == 8):
            self.delete_pawn(3-self.whose_turn)
            
        if ax==0:
            self.is_new_mill(tile,1)
            self.is_new_mill(tile,2)


    def play(self):
        while True:
            if(self.pawns_2_free>0):
                tile = self.place_pawn()
            elif((self.pawns_1_onboard==3 and self.whose_turn==1) or (self.pawns_2_onboard==3 and self.whose_turn==1)):
                self.delete_pawn(self.whose_turn)
                tile = self.place_pawn()
            else:
                tile = self.move_pawn()
            
            self.is_new_mill(tile)


            if (self.pawns_1_onboard+self.pawns_1_free==2):
                return 2
            elif(self.pawns_2_onboard+self.pawns_2_free==2):
                return 1
            
            self.whose_turn = 3-self.whose_turn



        
        


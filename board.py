class Board:
    def __init__(self):
        self.board = [0] * 24

    def print_board(self):
        temp = [[0,"_","_",1,"_", "_",2],
                ["_",8,"_",9,"_",10,"_"],
                ["_","_",16,17,18,"_","_"],
                [7,15,23,"_",19,11,3], 
                ["_","_",22,21,20,"_","_"],
                ["_",14,"_",13,"_",12,"_"],
                [6,"_","_",5,"_","_",4]]
        for row in temp:
            for tile in row:
                if tile=="_":
                    print("_", end="")
                else:
                    print(self.board[tile], end="")
            print()



    # axis x - 0 y -1 z - 2
    def get_mill(self, axis, tile):
        x,y,z = self.tile_to_xyz(tile)
        res = []
        if(axis == 0 and y!=1):
            res.append(self.board[self.xyz_to_tile(0,y,z)])
            res.append(self.board[self.xyz_to_tile(1,y,z)])
            res.append(self.board[self.xyz_to_tile(2,y,z)])
        elif(axis == 1 and x!=1):
            res.append(self.board[self.xyz_to_tile(x,0,z)])
            res.append(self.board[self.xyz_to_tile(x,1,z)])
            res.append(self.board[self.xyz_to_tile(x,2,z)])
        elif(axis == 2 and (x==1 or y==1)):
            res.append(self.board[self.xyz_to_tile(x,y,0)])
            res.append(self.board[self.xyz_to_tile(x,y,1)])
            res.append(self.board[self.xyz_to_tile(x,y,2)])
        else:
            return [-1,-1,-1]

        return res


    def get_neighbours(self,tile):
        x,y,z = self.tile_to_xyz(tile)
        res = []
        if(y!=1):
            if(x==1):
                res.append(self.board[self.xyz_to_tile(0,y,z)])
                res.append(self.board[self.xyz_to_tile(2,y,z)])
            else:
                res.append(self.board[self.xyz_to_tile(1,y,z)])

        if(x!=1):
            if(y==1):
                res.append(self.board[self.xyz_to_tile(x,0,z)])
                res.append(self.board[self.xyz_to_tile(x,2,z)])
            else:
                res.append(self.board[self.xyz_to_tile(x,1,z)])
                
        elif(x==1 or y==1):
            if(z==1):
                res.append(self.board[self.xyz_to_tile(x,y,0)])
                res.append(self.board[self.xyz_to_tile(x,y,2)])
            else:
                res.append(self.board[self.xyz_to_tile(x,y,1)])
        return res

                
    def tile_to_xyz(self, tile):
        z = tile//8
        if(tile%8==1 or tile%8==5):
            x = 1
        elif tile%8 in range(2,5):
            x = 2
        else:
            x = 0

        if(tile%8==7 or tile%8==3):
            y = 1
        elif tile%8 in range(4,7):
            y = 2
        else:
            y = 0

        return [x,y,z]
        

    def xyz_to_tile(self, x,y,z):
        if(x==2 and z == 2):
            print("tile does not exist")
        temp = [[0,7,6],[1,-1,5],[2,3,4]]

        return 8*z + temp[x][y]
            

        

import socket
import struct

class Server:
    def __init__(self):
        HOST = "0.0.0.0"
        PORT = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(1)
        print("Waiting for a connection...")
        self.connection, self.address = self.server.accept()
        print("Connected by:", self.address)

    def helper(self, board):
        #send board
        for tile in board.board:
            self.connection.sendall(struct.pack("!h", tile))


        data = self.connection.recv(1024)

        print("Received:", data.decode())
        return int(data.decode())
    
    def place_pawn(self,board):
        return self.helper(board)
    def delete_pawn(self, board,whose):
        return self.helper(board)
    def move_pawn(self,board):
        return self.helper(board),self.helper(board)
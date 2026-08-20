import socket
from board import Board
import struct

SERVER_IP = "192.168.1.68"
SERVER_PORT = 5000
b = Board()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, SERVER_PORT))

while True:

    for i in range(24):
        b.board[i] = struct.unpack("!h",client.recv(2))[0]


    b.print_board()
    data = input("Your move: ")

    client.sendall(data.encode())

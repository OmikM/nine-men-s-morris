from board import Board
from game import Game
from person import Person
from PlayFromFile import PlayFromFile
from RandomMoves import RandomMoves


p1 = Person()
#p1 = RandomMoves(1)
#p2 = Person()
#p2 = PlayFromFile("move_list/m1.txt")
p2 = RandomMoves(2)

game = Game(p1,p2)

print(game.play())



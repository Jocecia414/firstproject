import itertools as it
import csv
from moving_piece import Pieces

def main():
  
  game_size = 8
  game = []
  player_names = ["Zedan","Andrea"]
  
  
  board(game, game_size)
  results= reading_in_data()
  dictionaries = pieces()
  placing_initial_pieces(game,dictionaries[0], dictionaries[1])
  
  
  x = it.cycle(player_names)
  
  print('\nChess Match\n......................')
  display = Pieces(dictionaries, game, game_size)
  display.display_board()
  
  for list in results:
    piece = Pieces(list, game, game_size)
    print(f"Player 1: {next(x)} \nMove: {piece.white_piece}")
    move1 = piece.find_x_and_y_white()
    if len(list) == 1:
      move1
      piece.display_board()
      break
    print(f"\nPlayer 2: {next(x)} \nMove: {piece.black_piece}")
    move2 = piece.find_x_and_y_black()
    piece.display_board()
    choice = input("Continue? ")
    if choice == 'n':
      break
    
def board(game, game_size):
  #creates board with 8 X 8 lists with originally only . components
  for i in range(game_size):
    row = []
    for i in range(game_size):
       row.append('.')
    game.append(row)

  
def pieces():
    black_pieces = {'K': [(0, 3)], 'Q': [(0, 4)], 'B': [(0, 2), (0, 5)], 'N': [(0, 1), (0, 6)], 'R': [(0, 0), (0, 7)],
                    'P': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]}

    white_pieces = {'k': [(7, 3)], 'q': [(7, 4)], 'b': [(7, 2), (7, 5)], 'n': [(7, 1), (7, 6)], 'r': [(7, 0), (7, 7)],
                    'p': [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]}

    return black_pieces, white_pieces

def placing_initial_pieces(game, black_pieces, white_pieces):
  #iterates over dictionaries to place initial pieces
   for key,value in black_pieces.items():
       for item in value:
          x,y = item[0], item[1]
          game[x][y] = key
   for key,value in white_pieces.items():
       for item in value:
          x,y = item[0], item[1]
          game[x][y] = key


def reading_in_data():
    with open("/Users/jocelyngarcia/Desktop/Internship/problem 2/chess-moves.csv", "r") as file_input_CSV:
      #parses data into two seperate lists while discarding of starting element
      #list comprehension
        csv_reader = csv.reader(file_input_CSV)
        mylist= [ line for line in csv_reader ]
        mylist = [items[0].split(" ") for items in mylist]
        all_moves = [element[1:] for element in mylist]
        
      #returns both lists
    return all_moves


##Rook pieces move any number of square pieces whther horizontal or vertical
##knight is more complicated-- one piece perpindiculare than those two squares
##Bishop moves perpendicular any spaces

#possible_moves = {'r':[(0,1), (1,0)]}
#
#
#def get_rook_origins(game, r, c, move):
#        for i, row in enumerate(game):
#            for j, piece in enumerate(row):
#                if piece == move.piece_moved:
#                    row_dist = abs(r-i)
#                    col_dist = abs(c-j)
#                    if row_dist == 0 or col_dist == 0:
#                        coordinates = (i, j)
#        return coordinates
#    
#def get_knight_origins(self, r, c, move):
#        for i, row in enumerate(self.board):
#            for j, piece in enumerate(row):
#                if piece == move.piece_moved:
#                    row_dist = abs(r-i)
#                    col_dist = abs(c-j)
#                    if (row_dist == 1 and col_dist == 2) or (row_dist == 2 and col_dist == 1):
#                        coordinates = (i,j)
#        return coordinates
#
#def get_bishop_origins(self, r, c, move):
#        for i, row in enumerate(self.board):
#            for j, piece in enumerate(row):
#                if piece == move.piece_moved:
#                    row_dist = abs(r-i)
#                    col_dist = abs(c-j)
#                    if row_dist == col_dist:
#                        coordinates = (i,j)
#        return coordinates

#def get_queen_origins(self, r, c, move):
#        for i, row in enumerate(self.board):
#            for j, piece in enumerate(row):
#                if piece == move.piece_moved:
#                    row_dist = abs(r-i)
#                    col_dist = abs(c-j)
#                    if row_dist == 0 or col_dist == 0:
#                        coordinates = (i, j)
#                    if row_dist == col_dist:
#                        coordinates = (i, j)
#        return coordinates
#
#def get_king_origins(game, r, c, move):
#        for i, row in enumerate(game):
#            for j, piece in enumerate(row):
#                if piece == move.piece_moved:
#                    row_dist = abs(r-i)
#                    col_dist = abs(c-j)
#                    if row_dist <= 1 and col_dist <= 1:
#                        coordinates = (i, j)
#        return coordinates


if __name__ == '__main__':
    main()

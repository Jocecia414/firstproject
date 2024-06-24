
class Pieces():
    def __init__(self, moves, game, game_size):
        self.game = game
        self.game_size = game_size
        self.moves = moves

        self.letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        self.white_piece= self.moves[0]
        self.black_piece = self.moves[-1]
        self.key =''
        self.y = 0
        self.x = 0
        
    def find_x_and_y_white(self):
        if self.white_piece[0] in self.letters_to_numbers:
               self.key = 'p'
               self.y = self.letters_to_numbers.get(self.white_piece[0])
               if self.white_piece[1] == 'x':
                   self.captured(self.white_piece)
               else:
                   self.x = 8-int(self.white_piece[1])
                   self.game[self.x][self.y]= self.key
                   self.remove_initial_pawn()
        else:
           self.key = self.white_piece[0].lower()
           self.Rank_pieces(self.white_piece)
       
       
    def find_x_and_y_black(self):
        if self.black_piece[0] in self.letters_to_numbers:
               self.key = 'P'
               self.y = self.letters_to_numbers.get(self.black_piece[0])
               if self.black_piece[1] == 'x':
                   self.captured(self.black_piece)
               else:
                   self.x = 8-int(self.black_piece[1])
                   self.game[self.x][self.y]= self.key
                   self.remove_initial_pawn()
        else:
           self.key = self.black_piece[0] 
           self.Rank_pieces(self.black_piece) 
           #return 0
    
    def captured(self, piece):
        self.y = self.letters_to_numbers.get(piece[2])
        self.x =  8-int(piece[3])
        self.game[self.x][self.y] = self.key
        print("A piece was captured by player")
        if '+' in piece:
                     print("Player has put King in check!")
    
    def remove_initial_pawn(self):
        if self.key== 'p' or self.key == "P":
            for i in range(8):
                 if self.game[i][self.y] == self.key:
                          self.game[i][self.y] = "."
                          self.game[self.x][self.y] = self.key
        
    
    def Rank_pieces(self, piece):
        if piece[1] != 'x' :
                y = self.letters_to_numbers.get(piece[1] ) #switches out corresponding number notation from letter
                x = 8-int(piece[2])
                self.game[x][y] = self.key
                if "#" in piece:
                     print("CHECKMATE!!!")
                elif '+' in piece:
                     print("Player has put King in check!")
        else:
            self.captured(piece)
        
    
    def initial_position(self, x, y):
        pass
    def new_position(self):
        pass
    
    
    def display_board(self):
      #board goes from 8-1
      number_on_board = 8 
      #using ascii to get letters
      letter = 97
      print()
      for list in self.game:
        #string concatination
            print(str(number_on_board) + ' '*3, end='')
            number_on_board -= 1
            for element in list:
               print( element, end=" ")
            print()
    
      for length in range(self.game_size):
          if letter == 97:
              print('\n' +' '*3, end= " ")
          print(chr(letter), end =" ")
          letter += 1
    
      print()
  
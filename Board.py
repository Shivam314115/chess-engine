from Pieces import *
class Board:
    coords=['a','b','c','d','e','f','g','h']
    def __init__ (self):
        
        self.boardArr = [[None for i in range(9)] for j in range(9)]
        
    def initBoard(self):
        self.boardArr[0][0] = " "
        for i in range(1,9):
            self.boardArr[0][i]=Board.coords[i-1]
            self.boardArr[i][0] =9-i
            self.boardArr[2][i] = Pawn("white")
            self.boardArr[7][i]=Pawn("black")
        
        self.boardArr[1][1]=Rook("black")
        self.boardArr[1][8]=Rook("black")
        self.boardArr[8][1]=Rook("white")
        self.boardArr[8][8]=Rook("white")
        self.boardArr[1][2]=Knight("black")
        self.boardArr[1][7]=Knight("black")
        self.boardArr[8][2]=Knight("white")
        self.boardArr[8][7]=Knight("white")
        self.boardArr[1][3]=Bishop("black")
        self.boardArr[1][6]=Bishop("black")
        self.boardArr[8][3]=Bishop("white")
        self.boardArr[8][6]=Bishop("white")
        self.boardArr[1][5]=King("black")
        self.boardArr[1][4]=Queen("black")
        self.boardArr[8][5]=King("white")
        self.boardArr[8][4]= Queen("white")
        

    def printBoard(self):
            for i in range(0, 9):
                for j in range(0, 9):
                    # FIX 2: Added end=" " so elements in the same row print side-by-side
                    if i ==0 or j==0:
                        print(self.boardArr[i][j], end=" ")
                    elif self.boardArr[i][j] is None:
                        print(".",end=" ")
                    else:
                        print(self.boardArr[i][j].symbol, end=" ")
                print() # Prints a clean newline at the end of each row
            print("-" * 18) # Separator line to visually track output states



    def getPiece(self,text:str)->str:
        if len(text)!= 2:
            return "Invalid Square"
        text = text.lower()
        file = text[0]
        rank= text[1]
        if file not in self.coords or rank not in "12345678":
            return "invalid square"
        
        col = self.coords.index(file) +1
        row = 9-int(rank)
        
        return self.boardArr[row][col]
        
        
        
    def setPiece(self,piece: Piece, square:str)->str:
        if len(square)!=2:
            return "invalid square"
        
        square = square.lower()
        file = square[0]
        rank = square[1]
        if file not in self.coords or rank not in "12345678":
            return "invalid square"
        col = self.coords.index(file)+1
        row=9-int(rank)
        if self.boardArr[row][col] is not None:
            return "square already occupied"

        else:
            self.boardArr[row][col]= piece
            return f"piece:{piece.symbol}, color:{piece.color} set to square{square}"
        
        
    def removePiece(self,square:str)->str:
        if len(square)!=2:
            return "invalid square"
        square=square.lower()
        file=square[0]
        rank=square[1]
        if file not in self.coords or rank not in"12345678":
            return "invalid square"
        col = self.coords.index(file)+1
        row = 9-int(rank)
        
        if self.boardArr[row][col] is None:
            return f"no piece to remove on {square}"
        else:
            self.boardArr[row][col] = None


b1 = Board()

b1.initBoard()
b1.printBoard()
knight= b1.getPiece("G1")
print(knight)
b1.removePiece("g1")
b1.setPiece(knight, "f3")
b1.printBoard()

            
            
        


class Piece:
    
    def __init__ (self,color:str, symbol:str , value:float):
        self.color = color
        self.value = value
        self.symbol = symbol



class Knight(Piece):
    def __init__ (self, color:str ):
        super().__init__(color, "N", 2.75)
        
    
    


class Pawn(Piece):
    def __init__ (self, color:str):
        super().__init__(color, "P", 1.00)



class Bishop(Piece):
    def __init__ (self,color:str):
        super().__init__(color, "B", 3.25)


class King(Piece):
   
    def __init__ (self,color:str):
        super().__init__(color, "K", 500.00)


class Rook(Piece):
    def __init__(self,color:str):
        super().__init__(color,"R", 5.00)
        
           
class Queen(Piece):
    def __init__(self,color:str):
        super().__init__(color, "Q", 9.00)
       
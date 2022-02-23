
from carton import Carton

# Cette classe est vitale car elle determine comment marquer les cartons quand le joueur dispose de la carte tirée et comment on determine le(la) (les) vainqueurs


class isWinner:
    # Methode pour marquer le carton
    def mark(self, i, j, cartonX):
        if(0 < i > 4 or 0 < j > 4):
            raise ValueError('Invalid board position')
        if ('X' in cartonX[i][j]):
            raise ValueError('la position est deja occupee')
        print(cartonX[2][3])

        return cartonX[i][j] + " "+'X'
    # Verification d'une position gagnante

    def isWin(self, carton):
        if(('X' in self.mark(0, 0, carton) and 'X' in self.mark(0, 1, carton) and 'X' in self.mark(0, 2, carton) and 'X' in self.mark(0, 3, carton) and 'X' in self.mark(0, 4, carton)) or
            ('X' in self.mark(1, 0, carton) and 'X' in self.mark(1, 1, carton) and 'X' in self.mark(1, 2, carton) and 'X' in self.mark(1, 3, carton) and 'X' in self.mark(1, 4, carton)) or
            ('X' in self.mark(2, 0, carton) and 'X' in self.mark(2, 1, carton) and 'X' in self.mark(2, 2, carton) and 'X' in self.mark(2, 3, carton) and 'X' in self.mark(2, 4, carton)) or
           ('X' in self.mark(3, 0, carton) and 'X' in self.mark(3, 1, carton) and 'X' in self.mark(3, 2, carton) and 'X' in self.mark(3, 3, carton) and 'X' in self.mark(3, 4, carton)) or
            ('X' in self.mark(4, 0, carton) and 'X' in self.mark(4, 1, carton) and 'X' in self.mark(4, 2, carton) and 'X' in self.mark(4, 3, carton) and 'X' in self.mark(4, 4, carton)) or
            ('X' in self.mark(0, 0, carton) and 'X' in self.mark(1, 0, carton) and 'X' in self.mark(2, 0, carton) and 'X' in self.mark(3, 0, carton) and 'X' in self.mark(4, 0, carton)) or
            ('X' in self.mark(0, 1, carton) and 'X' in self.mark(1, 1, carton) and 'X' in self.mark(2, 1, carton) and 'X' in self.mark(3, 1, carton) and 'X' in self.mark(4, 1, carton)) or
            ('X' in self.mark(0, 2, carton) and 'X' in self.mark(1, 2, carton) and 'X' in self.mark(2, 2, carton) and 'X' in self.mark(3, 2, carton) and 'X' in self.mark(4, 2, carton)) or
            ('X' in self.mark(0, 3, carton) and 'X' in self.mark(1, 3, carton) and 'X' in self.mark(2, 3, carton) and 'X' in self.mark(3, 3, carton) and 'X' in self.mark(4, 3, carton)) or
            ('X' in self.mark(0, 4, carton) and 'X' in self.mark(1, 4, carton) and 'X' in self.mark(2, 4, carton) and 'X' in self.mark(3, 4, carton) and 'X' in self.mark(4, 4, carton)) or
            ('X' in self.mark(0, 0, carton) and 'X' in self.mark(1, 1, carton) and 'X' in self.mark(2, 2, carton) and 'X' in self.mark(3, 3, carton) and 'X' in self.mark(4, 4, carton)) or
            ('X' in self.mark(0, 4, carton) and 'X' in self.mark(1, 3, carton) and 'X' in self.mark(2, 2, carton) and 'X' in self.mark(3, 1, carton) and 'X' in self.mark(4, 0, carton)) or
                ('X' in self.mark(0, 0, carton) and 'X' in self.mark(4, 0, carton) and 'X' in self.mark(0, 4, carton) and 'X' in self.mark(4, 4, carton))):
            return True

    def winner(self):
        if isWinner == True:
            return "Nous avons un gagnant"
        else:
            return None

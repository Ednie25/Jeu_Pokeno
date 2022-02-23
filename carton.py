from cartes import Carte

# Contruction de la classe carton


class Carton:
    # constructeur pour la classe carton
    def __init__(self):
        self.carton = []
    # definition des cartons: Il faut preciser qu'il se construit a partir des cartes tirés aleatoirement

    def cartonX(self, carte):
        self.carton = [['']*5 for j in range(5)]
        for i in range(5):
            for j in range(5):
                self.carton[i][j] = carte.tirage_aleatoire(
                    carte.carte_noire, carte.carte_rouge)
        return self.carton

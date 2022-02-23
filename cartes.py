import random


class Carte:  # cette classe sert à construire les cartes qui sont les premiers éléments du jeu
    # contruction carte rouge
    # on avait pas besoin de faire les constructions de carte pour chaque couleur séparément on aurait pu avoir des boucles imbriquées
    def carte_rouge(self, couleur='rouge'):
        carte = []
        numero = [i for i in ('as', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', 'j', 'q', 'k')]  # ce sont les treize numeros qui forment le Jeu de cartes
        figure = [j for j in ('coeur', 'carreau')]
        for i in numero:
            for j in figure:
                carte.append(i+" de "+j + " rouge")
        return carte

        # contruction carte noire
    def carte_noire(self, couleur='noire'):
        carte = []
        numero = [i for i in ('as', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', 'j', 'q', 'k')]  # ce sont les treize numeros qui forment le Jeu de cartes
        figure = [j for j in ('piques', 'trefles')]
        for i in numero:
            for j in figure:
                carte.append(i+" de "+j + " noire")
        return carte

    # Cette methode sert à tirer une carte aleatoire dans le jeu. Nous ferons beaucoup appel a cette methode pour la suite
    def tirage_aleatoire(self, carte_rouge, carte_noire):
        carte_rouge2 = carte_rouge("rouge")
        carte_noire2 = carte_noire("noire")
        # tirage aleatoire parmi les cartes rouges
        tirage_rouge = random.choice(carte_rouge2)
        # tirage aleatoire parmi les cartes noires
        tirage_noir = random.choice(carte_noire2)
        # tirage de la carte finale
        return random.choice((tirage_noir, tirage_rouge))

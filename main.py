from cartes import Carte
from carton import Carton
from winRules import isWinner

jeu_de_carte = Carte()
carton = Carton()
regleDuJeu = isWinner()

carton2 = carton.cartonX(jeu_de_carte)
carton3 = carton.cartonX(jeu_de_carte)

nombreDeCarte = 0

print("*"*30, "Bienvenu dans le jeu POKENO", "*"*30)
inputUser = input("Appuyer sur r pour lire les regles: ")
if(inputUser != "r"):
    print("vous n'avez pas appuye sur r")
    input("Appuyer sur r pour lire les regles")
print("---"*30)

print("Le jeu POKENO est simple, vous avez un carton constitue de cartes et des cartes sont tires aleatoirement dans un jeu de carte. Si vous avez la bonne disposition de carte, vous gagnez")
print("---"*30)
print("Vous allez entrer votre nom")
print("---"*30)

user_name1 = input("Entrer votre nom: ")
print("---"*30)

user_name2 = input("Entrer votre nom: ")
print("---"*30)

joueurs = (user_name1, user_name2)
print("Pour", user_name1, "Le carton est:")
print("---"*30)

print(carton2)
print("---"*30)
print("---"*30)

print("Pour", user_name2, "Le carton est:")
print(carton3)
print("---"*30)
print("---"*30)

while nombreDeCarte <= 52:
    EtatDuJeu1 = False
    EtatDuJeu2 = False
    carte = jeu_de_carte.tirage_aleatoire(Carte.carte_noire, Carte.carte_rouge)

    print("Nous allons marquer le carton de", user_name1)

    for i in range(4):
        for j in range(4):
            if carton2[i][j] == carte:
                mark = regleDuJeu.mark(i, j, carton2)
            else:
                continue
    print(carton2)

    print("Nous allons marquer le carton de", user_name2)

    for i in range(4):
        for j in range(4):
            if carton3[i][j] == carte:
                regleDuJeu.mark(i, j, carton3)
            else:
                continue
    print(carton3)
    EtatDuJeu1 = regleDuJeu.isWin(carton2)
    EtatDuJeu2 = regleDuJeu.isWin(carton3)

    if(EtatDuJeu1 == True):
        print(user_name1, " ", "a gagne")
    if(EtatDuJeu2 == True):
        print(user_name2, " ", "a gagne")
    nombreDeCarte = nombreDeCarte+1
    break
print("break")
print("*"*30, "Merci d'avoir participe", "*"*30)

from grid import Grid
from graph import Graph
from random import randrange
from solver import Solver
from Graph_rep import Graphics

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


# jeu auquel on peut jouer qu'à partir d'un certain niveau de difficulté (j'ajouterai le graphique quand ça marchera)
#préciser jusqu'à combien de lignes/colonnes on peut jouer

def game():
    # on détermine forme matrice et solution
    lines = int(input("nombre de lignes: "))
    columns = int(input("Nombre de colonnes: "))
    destination= Graphics.construction_ex(lines, columns)
    # déterminer le bon lambda pour utiliser A* ( voir fonction Adrien)
    # choix de la difficulté ( facile = peu de swaps, moyen = plus de swaps, dur = + de swap et des barrières)
    level = input("Tapez 'facile', 'moyen' ou 'difficile' :")
    if level == "facile":
        while solution >3:
        range = randrange(1,lines*columns)    #pour prendre une matrice au hasard il faudrai plutot tirer un nb au hasard entre 0 et (m*n)!-1
        all = Graph.generate_matrices(lines, columns)
        for_game = all[range]
    # déterminer le nb de swaps optimal (et afficher que c'est le nombre de swaps nécessaire pour gagner=> en bas du pygame ?)
        solution = Graph.a_star(self, for_game, destination) # en rajoutant un truc pour que retourne nb de swaps optimaux
    elif level == "moyen":
        while solution <4:
        range = randrange(1,lines*columns)
        all = Graph.generate_matrices(lines, columns)
        for_game = all[range]
    # déterminer le nb de swaps optimal (et afficher que c'est le nombre de swaps nécessaire pour gagner=> en bas du pygame ?)
        solution = Graph.a_star(self, for_game, destination) # en rajoutant un truc pour que retourne nb de swaps optimaux
    elif level == "difficile": #voir selon si on a le temps de faire les barrières
    # modéliser la grille avec pygame, avec tous les trucs nécessaires, rajouter l'option réussite et l'options pas réussite
    Graphics.display_pygame(for_game, solution)
    


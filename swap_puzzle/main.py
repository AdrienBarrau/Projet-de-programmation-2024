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
    # regle = ...
    print(regles)
    lines = int(input("nombre de lignes: "))
    columns = int(input("Nombre de colonnes: "))
    # déterminer le bon lambda pour utiliser A* ( voir fonction Adrien)
    # choix de la difficulté ( facile = peu de swaps, moyen = plus de swaps, dur = + de swap et des barrières)
    level = input("Tapez 'facile', 'moyen' ou 'difficile' :")
    if level == "facile":
        solution=100
        while solution >2:
            range = randrange(1,lines*columns)    #pour prendre une matrice au hasard il faudrai plutot tirer un nb au hasard entre 0 et (m*n)!-1
            all = Graph.generate_matrices(lines, columns)
            for_game = all[range]
    # déterminer le nb de swaps optimal
            if lines + columns <= 4:
                solution = time_and_solve_new_bfs([for_game])[0][2]
            elif lines + columns > 4:
                solution = time_and_solve_a_star([for_game])[0][2]
        print("Pour gagner, vous devez ordonner la grille en "+ str(solution) + "swaps")
        # modéliser la grille avec pygame, avec tous les trucs nécessaires, rajouter l'option réussite et l'options pas réussite
        Graphics.display_pygame(for_game, solution)
    elif level == "moyen":
        solution=-100
        while solution <=2:
            range = randrange(1,lines*columns)
            all = Graph.generate_matrices(lines, columns)
            for_game = all[range]
            if lines + columns <= 4:
                solution = time_and_solve_new_bfs([for_game])[0][2]
            elif lines + columns > 4:
                solution = time_and_solve_a_star([for_game])[0][2]
        print("Pour gagner, vous devez ordonner la grille en "+ str(solution) + "swaps")
        # modéliser la grille avec pygame, avec tous les trucs nécessaires, rajouter l'option réussite et l'options pas réussite
        Graphics.display_pygame(for_game, solution)
    elif level == "difficile": #voir selon si on a le temps de faire les barrières
        range = randrange(1,lines*columns)
        all = Graph.generate_matrices(lines, columns)
        for_game = all[range]
        number_walls= int(input("Combien de murs voulez vous insérez ( au maximum, vous pouvez en mettre"+ str(columns*(lines-1) + lines*(columns-1)- 3)+ ": "))
        gfor_game = Grid(lines, columns, for_game)
        walls= gfor_game.creation_walls(number_walls)
        walls_i= walls[0]
        walls_j= walls[1]
        print("Vous ne pouvez pas swapper les cases: ")
        for a in range(len(walls_i)):
            print(str(walls_i[a])+ "et"+ str(walls_j[a]))
        Graphics.display_pygame(for_game, walls)
            
        
        
    
    


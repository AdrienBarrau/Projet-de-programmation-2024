from grid import Grid
from graph import Graph
import random
import time

class Solver(): # chemin_grille est une liste de tuples de tuples contenant le chemin des grilles parcouru
          
    def __init__(self, chemin_grille=[]):
        self.chemin_grille=chemin_grille

    def affiche_matrices(self):   #affiche le chemin de matrices
        print(self.chemin_grille)

    def get_solution(self):   #retourne les swaps a effectuer
        #print("\n")
        liste=self.chemin_grille
        res=[]   #liste des swaps
        for k in range(0,len(liste)-1):
            tmp=[]
            for i in range (len(liste[0])):   #len(liste[0]) est le nb de lignes
                for j in range (len(liste[0][0])):  #len(liste[0][0]) est le nb de colonnes
                    if not(liste[k][i][j]==liste[k+1][i][j]):
                        tmp=tmp+[(i,j)]
            res=res+[tuple(tmp)]
        #print("Il y'a",len(res),"swaps pour resoudre la grille")
        return res

#nos fonctions solutions étant construitent, on veut en évaluer la plus value par rapport à la solution naive, qui est très imprécise mais imbattable en temps d'éxécution
# Pour cela on va utiliser nos solutions sur des matrices choisi au hasard de taille m*n avec m et n raisonnablement petits



def time_and_swaps_bfs(liste_mat):     #pour une liste de matrices, on calcule combien de temps le bfs amélioré met de temps, et combien swaps contient son chemin le plus court (optimal)
    res=[]
    for i in range (len(liste_mat)):    # on renvoi un liste de quadruplets contenant (le temps de resolution, la liste des swaps,le nombre de swaps, la matrice)
        m=len(liste_mat[i])
        n=len(liste_mat[i][0])              # détermination des dimensions de la matrice
        grille=Grid(m,n,liste_mat[i])
        deb=time.time()
        chemin=Solver(Graph.solve_bfs(grille)) 
        fin=time.time()
        tps=fin-deb
        swaps=chemin.get_solution()
        res.append((tps,swaps,len(swaps),liste_mat[i]))
    return res

def time_and_solve_new_bfs(liste_mat):     #pour une liste de matrices, on calcule combien de temps le bfs amélioré met de temps, et combien swaps contient son chemin le plus court (optimal)
    res=[]
    for i in range (len(liste_mat)):    # on renvoi un liste de quadruplets contenant (le temps de resolution, la liste des swaps,le nombre de swaps, la matrice)
        m=len(liste_mat[i])
        n=len(liste_mat[i][0])              # détermination des dimensions de la matrice
        grille=Grid(m,n,liste_mat[i])
        deb=time.time()
        chemin=Solver(Graph.solve_new_bfs(grille)) 
        fin=time.time()
        tps=fin-deb
        swaps=chemin.get_solution()
        res.append((tps,swaps,len(swaps),liste_mat[i]))
    return res

def time_and_solve_a_star(liste_mat):     #pour une liste de matrices, on calcule combien de temps le bfs amélioré met de temps, et combien swaps contient son chemin le plus court (optimal)
    res=[]
    for i in range (len(liste_mat)):    # on renvoi un liste de quadruplets contenant (le temps de resolution, la liste des swaps,le nombre de swaps, la matrice)
        m=len(liste_mat[i])
        n=len(liste_mat[i][0])              # détermination des dimensions de la matrice
        grille=Grid(m,n,liste_mat[i])
        deb=time.time()
        chemin=Solver(Graph.solve_a_star(grille)) 
        fin=time.time()
        tps=fin-deb
        swaps=chemin.get_solution()
        res.append((tps,swaps,len(swaps),liste_mat[i]))
    return res

def generate_random_matrices(m,n,nb):         # (m,n) sont les dimensions des matrices et nb le nombre qu'on veut générer
    res=[]     #liste de matrices aléatoire de taille (m,n)
    nombres=[i+1 for i in range(m*n)]
    for i in range(nb):
        matrice=[]
        random.shuffle(nombres)     #on mélange les (m*n) numéros
        for i in range(m):
            ligne=nombres[i*n:(i+1)*n]    #on remplie chaque ligne avec n d'entre eux, et ce m fois
            matrice.append(ligne)              #on ajoute une ligne a la matrice 

        res.append(matrice)          #on ajoute la matrice a la liste res

    return res

#print(generate_random_matrices(3,9,5))    #fonctionne bien

#liste_mat=generate_random_matrices(2,3,100)
liste_mat=Graph.generate_matrices(2,2)
liste_mat.remove([[i*2+j+1 for j in range (2)] for i in range (2)])
#(time_and_swaps_bfs(liste_mat))
#time_and_solve_new_bfs(liste_mat)
#time_and_solve_a_star(liste_mat)

def write_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"Temps: {result[0]}, Swaps: {result[1]}, Nombre de swaps: {result[2]}\n")
            file.write(f"Matrix:\n")
            for ligne in result[3]:
                file.write(f"{ligne}\n")
            file.write("\n")


write_results_to_file(time_and_solve_new_bfs(liste_mat), "new_bfs_2_2_results.txt")




'''  tests
grille_ex=Grid(2,2,[[1,2],[3,4]])
chemin1=Solver(Graph.solve_bfs(grille_ex)) 


print(chemin1.get_solution())  #donne la liste des swaps a effectuer
chemin1.affiche_matrices()

#print(grille_ex.get_solution_naive()) #meme nombre de swaps pour une grille 2 sur 2 : 4 swaps



#grille_ex2=Grid(3,3,[[9,8,7],[6,5,4],[3,2,1]])
#chemin2=Solver(Graph.solve_bfs(grille_ex2)) 


#print(chemin2.get_solution())           #16 swaps pour une grille 3 sur 3
#chemin2.affiche_matrices()

#print(grille_ex2.get_solution_naive())  #18 swaps pour une grille 3 sur 3


grille_ex4=Grid(5,5,[[25,24,23,21,22],[20,16,15,14,13],[19,12,11,10,9],[17,8,7,6,5],[18,4,3,2,1]])
chemin4=Solver(Graph.solve_a_star(grille_ex4))
print(chemin4.get_solution())

'''
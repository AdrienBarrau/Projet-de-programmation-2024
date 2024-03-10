from grid import Grid
from graph import Graph
import random
import time
import statistics
import numpy as np

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

def time_and_solve_naive(liste_mat):     #pour une liste de matrices, on calcule combien de temps le bfs amélioré met de temps, et combien swaps contient son chemin le plus court (optimal)
    res=[]
    for i in range (len(liste_mat)):    # on renvoi un liste de quadruplets contenant (le temps de resolution, la liste des swaps,le nombre de swaps, la matrice)
        m=len(liste_mat[i])
        n=len(liste_mat[i][0])              # détermination des dimensions de la matrice
        grille=Grid(m,n,liste_mat[i])
        deb=time.time()
        swaps=Grid.get_solution_naive(grille)
        fin=time.time()
        tps=fin-deb
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


'''generation de la database dans un fichier txt
#liste_mat=generate_random_matrices(2,3,100)
liste_mat=Graph.generate_matrices(2,2)
liste_mat.remove([[i*2+j+1 for j in range (2)] for i in range (2)])
time_and_solve_new_bfs(liste_mat)
def write_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"Temps: {result[0]}, Swaps: {result[1]}, Nombre de swaps: {result[2]}\n")
            file.write(f"Grille:\n")
            for ligne in result[3]:
                file.write(f"{ligne}\n")
            file.write("\n")
#write_results_to_file(time_and_solve_new_bfs(liste_mat), "new_bfs_2_2_results.txt")       data base (2,2),(3,2) et (2,3)
write_results_to_file(time_and_solve_a_star(liste_mat), "new_bfs_2_2_results.txt")
'''


def naive_performance(liste_mat):    #teste les perfs de solution_naive sur nb grilles de taille m,n

  tps=[]
  swaps=[]
  m=len(liste_mat[0])
  n=len(liste_mat[0][0])
  id=[[i*n+j+1 for j in range (n)] for i in range (m)]

  for mat in liste_mat :
    if not (mat==id):
      naive_result = time_and_solve_naive([mat])
      tps.append(naive_result[0][0])
      swaps.append(naive_result[0][2])
      
  tps_moy = statistics.mean(tps)
  swaps_moy = statistics.mean(swaps)
  print(f"Temps moyen de solution_naive : {tps_moy}, nb swaps moyen: {swaps_moy}")

def new_bfs_performance(liste_mat):    #teste les perfs de solution_naive sur nb grilles de taille m,n
  tps=[]
  swaps=[]
  m=len(liste_mat[0])
  n=len(liste_mat[0][0])
 
  id=[[i*n+j+1 for j in range (n)] for i in range (m)]
    
  for mat in liste_mat :
    if not (mat==id):
      new_bfs_result = time_and_solve_new_bfs([mat])
      tps.append(new_bfs_result[0][0])
      swaps.append(new_bfs_result[0][2])

  tps_moy = statistics.mean(tps)
  swaps_moy = statistics.mean(swaps)
  print(f"Temps moyen de solution_new_bfs : {tps_moy}, nb swaps moyen: {swaps_moy}")

def a_star_performance(liste_mat):    #teste les perfs de a_star sur nb grilles de taille m,n
  tps=[]
  swaps=[]
  m=len(liste_mat[0])
  n=len(liste_mat[0][0])
  id=[[i*n+j+1 for j in range (n)] for i in range (m)]
  
  for mat in liste_mat :
    if not (mat==id):
      a_star_result = time_and_solve_a_star([mat])
    
      tps.append(a_star_result[0][0])
      swaps.append(a_star_result[0][2])
    
  tps_moy = statistics.mean(tps)
  swaps_moy = statistics.mean(swaps)
  print(f" temps moyen de A star: {tps_moy}, nb swaps moyen: {swaps_moy}")


'''modifiez liste_mat ci dessous pour etudier les performances des solutions! '''

liste_mat=generate_random_matrices(3,2,100)    #les deux premiers arguments donnent les dimensions, le troisieme est le nombre de matrices aleatoires


  
'''ne pas modifier'''
new_bfs_performance(liste_mat)
a_star_performance(liste_mat)
naive_performance(liste_mat)

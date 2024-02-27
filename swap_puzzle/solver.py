from grid import Grid
from graph import Graph

class Solver(): # chemin_grille est une liste de tuples de tuples contenant le chemin des grilles parcouru
          
    def __init__(self, chemin_grille=[]):
        self.chemin_grille=chemin_grille

    def affiche_matrices(self):   #affiche le chemin de matrices
        print(self.chemin_grille)

    def get_solution(self):   #retourne les swaps a effectuer
        print("\n")
        liste=self.chemin_grille
        res=[]   #liste des swaps
        for k in range(0,len(liste)-1):
            tmp=[]
            for i in range (len(liste[0])):   #len(liste[0]) est le nb de lignes
                for j in range (len(liste[0][0])):  #len(liste[0][0]) est le nb de colonnes
                    if not(liste[k][i][j]==liste[k+1][i][j]):
                        tmp=tmp+[(i,j)]
            res=res+[tuple(tmp)]
        print("Il y'a",len(res),"swaps pour resoudre la grille")
        return res





grille_ex=Grid(2,2,[[4,3],[2,1]])
chemin1=Solver(Graph.solve_bfs(grille_ex)) 


print(chemin1.get_solution())  #donne la liste des swaps a effectuer
chemin1.affiche_matrices()

#print(grille_ex.get_solution_naive()) #meme nombre de swaps pour une grille 2 sur 2 : 4 swaps



grille_ex2=Grid(3,3,[[9,8,7],[6,5,4],[3,2,1]])
chemin2=Solver(Graph.solve_bfs(grille_ex2)) 




print(chemin2.get_solution())           #16 swaps pour une grille 3 sur 3
chemin2.affiche_matrices()

#print(grille_ex2.get_solution_naive())  #18 swaps pour une grille 3 sur 3



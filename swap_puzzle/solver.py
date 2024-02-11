from grid import Grid
from graph import Graph
class Solver(): 
         # chemin_grille est une liste de tuples de tuples contenant le chemin des grilles parcouru
           
    def __init__(self, chemin_grille=[]):
        self.chemin_grille=chemin_grille

    def get_solution(self):
        liste=self.chemin_grille
        res=[]   #liste des swaps
        for k in range(0,len(liste)-1):
            tmp=[]
            for i in range (len(liste[0])):   #len(liste[0]) est le nb de lignes
                for j in range (len(liste[0][0])):  #len(liste[0][0]) est le nb de colonnes
                    if not(liste[k][i][j]==liste[k+1][i][j]):
                        tmp=tmp+[(i,j)]
            res=res+[tuple(tmp)]
        return res

grille_ex=Grid(2,2,[[4,3],[2,1]])
chemin1=Solver(Graph.solve_bfs(grille_ex))
print(chemin1.get_solution())

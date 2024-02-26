"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import numpy as np


class Grid():
    """
    A class representing the grid from the self. puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    m=0
    n=0
    state=[[]]
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = "The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def show(self):
        print(np.matrix(self.state))

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        m=self.m
        n=self.n
        for i in range (m):
            for j in range (n):        
                if not (self.state[i][j]==i*n+j+1):   
                    return False
        return True



    def swap(self, cell1, cell2):
        """
        Implements the self. operation between two cells. Raises an exception if the self. is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to self.. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        (i1,j1)=cell1
        (i2,j2)=cell2
        if ((((i1==i2) and abs(j1-j2)==1) or ((j1==j2) and abs(i1-i2)==1)) 
        and (i1,i2 <= self.n-1) and (j1,j2 <= self.m-1)and (i1,i2 >= 0) and (j1,j2 >= 0)):
            tmp=self.state[i1][j1]
            self.state[i1][j1]=self.state[i2][j2]
            self.state[i2][j2]=tmp


    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of self.s. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of self.s, each self. being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range (len(cell_pair_list)):
            (cell1,cell2)=cell_pair_list[i]
            self.swap(cell1,cell2)
    
    def adjacent_grids(self):    #renvoi une liste des matrices correspondants aux etats atteignables en 1 swap
        m=self.m
        n=self.n
        res=[]
        for i in range(m):
            for j in range(n):
                if (i==m-1 and j==n-1 ):  # coin bas a droite
                    ()
                   
                                                                    #on stocke une grille adjacente puis on reviens sur la grille initiale
                                                                      # Pour éviter les doublons on fait des swaps uniquement vers la droite ou en bas
                elif (i==m-1 and j==0 ):    #coin bas gauche
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                elif (i==0 and j==0 ):  #coin haut gauche
                    
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
                elif (i==0 and j==n-1): #coin haut droit
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
                elif (i==0 ): # premiere ligne
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                elif (i==m-1 ): # derniere ligne
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                elif (j==0 ): #1ere colonne
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                elif (j==n-1): #derniere colonne
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
                else:        #cas general
                    self.swap((i,j),(i,j+1))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i,j+1))
                    self.swap((i,j),(i+1,j))
                    res.append([ligne[:] for ligne in self.state])
                    self.swap((i,j),(i+1,j))
        return Grid.del_doublons(res)



    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
    
    def del_doublons(liste):
        new_liste = [] 
        for i in range (len(liste)): 
            if liste[i] not in new_liste: 
                new_liste.append(liste[i]) 
        return new_liste
        
    
    def go_to(self,cell1,cell2):     # on va d'abord a droite(ou a gauche) puis en haut!
        
        (i,j)=cell1
        (i1,j1)=cell2
        res=[]
        while not (j==j1):    #on traite d'abord les colonnes pour ne pas casser le tri
            if (j>j1):
                self.swap((i,j),(i,j-1))       #on se rapproche de la cible
                res=res+[tuple([(i,j),(i,j-1)])]
                j=j-1
            else:
                self.swap((i,j),(i,j+1))       #on se rapproche de la cible
                res=res+[tuple([(i,j),(i,j+1)])]
                j=j+1
        while not (i==i1): 
              
            if (i>i1):
                self.swap((i-1,j),(i,j))       #on se rapproche de la cible
                res=res+[tuple([(i-1,j),(i,j)])]
                i=i-1
            else:
                self.swap((i+1,j),(i,j-1))       #on se rapproche de la cible
                res=res+[tuple([(i+1,j),(i,j)])]
                i=i+1
        return res

    def get_solution_naive(self):
        m=self.m 
        n=self.n
        res=[]
        k=1    #k va de 1 jusqu'a n*m-1
        while not (self.is_sorted()):
            for i in range (m):
                for j in range(n):
                    if (self.state[i][j]==k):   # k=i1*n+j1+1  donc k-1=i1*n+j1
                        
                        i1=int((k-1)/n)      #quotient de la division euclidienne de k-1 par n
                        j1=(k-1)%n      #reste dans la division euclidienne de k-1 par n
                        res=res+self.go_to((i,j),(i1,j1))   #on deplace la case (i,j) vers (i1,j1)
                        k=k+1
                
        return res


#faire un random_grid_generator
            


def tests_swap(m,n,i1,j1,i2,j2,state):

    Grille_ex=Grid(m,n,state)
    Grille_ex.swap((i1,j1),(i2,j2))
    Grille_ex.show()
  
def tests_swap_seq(m,n,liste_swap,state):

    Grille_ex=Grid(m,n,state)
    Grille_ex.show()
    Grille_ex.swap_seq(liste_swap)
    Grille_ex.show()



def test_solution_naive(m,n,state):   # on a forcement len(res)<(m+n)*m*n
    Grille_ex2=Grid(m,n,state)
    print(Grille_ex2)
    print(Grille_ex2.get_solution_naive())
   
    


#tests_swap_seq(3,3,[((0,0),(0,1)),((1,2),(1,1))],[[9,8,7],[6,5,4],[3,2,1]])

test_solution_naive(4,4,[[15,14,13,12],[9,8,7,10],[11,6,5,4],[16,3,2,1]]) 



"""
grille_ex=Grid(2,2,[[1,2],[3,4]])
print(grille_ex.adjacent_grids())


# graphique ( question 4 je crois)
import matplotlib.pyplot as plt


# définition d'une grille
BROUILLON idée
def affiche(grille):
    #initialisation des paramètre
    fig, ax = plt.subplots()
    #création du nombre de compartiment avec texte
    ax.set_xticks(range(len(grille[0])))
    ax.set_yticks(range(len(grille)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    for i in range(len(grille[0])):
        for j in range (len(grille)):
            ax.text( i, j,grille[j][i])
    # ajout grille
    plt.grid(True,linewidth=2)
    plt.show()


ex_grille = [[1,2,3],[4,5,6]]
affiche(ex_grille)

grille=[[1,2,3],[4,5,6]]

#initialisation des paramètre
fig, ax = plt.subplots()
#création du nombre de compartiment avec texte
ax.set_xticks(range(len(grille[0])))
ax.set_yticks(range(len(grille)))
ax.set_xticklabels([])
ax.set_yticklabels([])
for i in range(len(grille[0])):
    for j in range (len(grille)):
        ax.text( i, j,grille[j][i])
# ajout grille
plt.grid(True,linewidth=2)
plt.show()





#affichage avec méthode de pygame

pip install pygame
# avec la méthode pygame
# imports
import pygame
import sys
pygame.init()

# création d'une fenêtre d'affichage
screen = pygame.display.set_mode((400,600))

# modélisation tableau

nb_lignes = 2
nb_colonnes = 3
ex_tabl= [[1,2,3],[4,5,6]]
click=0


def tableau(obj):
    for x in range(0,nb_lignes+1):
        pygame.draw.line(screen, (0, 0, 0), (x*200, 0),(x*200, 600))
    for y in range(0, nb_colonnes + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, y*200), (400, y*200))
    
    #affichage des chiffres
    font= pygame.font.SysFont(None, 45)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            number = font.render(str(obj[i][j]), True, (0,0,0), background= None)
            numb_position = number.get_rect(center=(j*200+100, i*200+100))
            screen.blit(number, numb_position)


# boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # essai de construction d'une grille intéractive
        if event.type == pygame.MOUSEBUTTONDOWN:
            if click== 0:
                click = 1
                f_position = pygame.mouse.get_pos()
                case_f_i= f_position[1]//200
                case_f_j= f_position[0]//200
                case_f = obj[case_f_i][case_f_j]
            elif click==1:
                click=0
                s_position= pygame.mouse.get_pos()
                case_s_i= s_position[1]//200
                case_s_j= s_position[0]//200
                case_s = obj[case_s_i][case_s_j]
                swap(case_f,case_f)
                # ici je suis pas sûre que juste swaper suffit pour changer représentation mmm
            

            

# fond blanc
    screen.fill((255, 255, 255))

# affichage du tableau
    tableau(ex_tabl)
    pygame.display.flip()


# fin pygame
pygame.quit()
sys.exit()

"""

#grille_test=Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
#print(grille_test.adjacent_grids())

#tests_swap_seq(3,3,[((0,0),(0,1)),((1,2),(1,1))],[[9,8,7],[6,5,4],[3,2,1]])

test_solution_naive(4,4,[[15,14,13,12],[9,8,7,10],[11,6,5,4],[16,3,2,1]])
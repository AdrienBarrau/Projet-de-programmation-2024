"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import numpy as np
from random import randrange


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
        else:
            return "Impossible"
            
    def identification(self,cell):
        (i,j)= cell
        id = i*len(self.state[0]) + j
        return id
        
    def origin_id(self, id):
        for line in range(len(self.state)):
            if line*len(self.state[0])<= id<(line+1)*len(self.state[0]):
                i= line
        j= id - i*len(self.state[0])
        cell= [i,j]
        return cell

    def creation_walls(self, nombre):
        liste_walls_i= [[-100,-100]]
        liste_walls_j= [[-100,-100]]
        cell1 = [-100,-100]
        cell2= [-100,-100]
        for wall in range(nombre):
            for idem in range(len(liste_walls_i)):
                while (cell1 == liste_walls_i[idem] and cell2 == liste_walls_j[idem]) or (cell1 == liste_walls_i[idem] and cell2 == liste_walls_j[idem]):
                    new_wall_i = random.randrange(len(self.state)*len(self.state[0])- 1)
                    new_wall_j=-100
                    while new_wall_j != new_wall_i +1 and new_wall_j != new_wall_i -1 and new_wall_j != new_wall_i +3 and new_wall_j != new_wall_i -3:
                        new_wall_j = random.randrange(len(self.state)*len(self.state[0])- 1)
                    cell1 = self.origin_id(new_wall_i)
                    cell2= self.origin_id(new_wall_j)
            liste_walls_i.append(cell1)
            liste_walls_j.append(cell2)
        liste_walls_i.pop(0)
        liste_walls_j.pop(0)
        walls= [liste_walls_i, liste_walls_j]
        return walls       

    def swap_when_walls(self, cell1, cell2, walls):
        liste_walls_i = walls[0] # garder comme ça
        liste_walls_j= walls[1]
        
        (i1,j1)=cell1
        (i2,j2)=cell2
        if ((((i1==i2) and abs(j1-j2)==1) or ((j1==j2) and abs(i1-i2)==1)) and (all(i1 !=liste_walls_i[index][0] or j1 !=liste_walls_i[index][1] or 
        i2 !=liste_walls_j[index][0] or j2 !=liste_walls_j[index][1] for index in range(len(liste_walls_i)))) and (all(i1 !=liste_walls_j[index][0] or 
        j1 !=liste_walls_j[index][1] or i2 !=liste_walls_i[index][0] or j2 !=liste_walls_i[index][1] for index in range(len(liste_walls_i))))
        and (i1,i2 <= self.n-1) and (j1,j2 <= self.m-1)and (i1,i2 >= 0) and (j1,j2 >= 0)):
            tmp=self.state[i1][j1]
            self.state[i1][j1]=self.state[i2][j2]
            self.state[i2][j2]=tmp
        else:
            return "Impossible"
    



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
    
    def adjacent_grids(self):
        m = self.m
        n = self.n
        res = []
        for i in range(m):
            for j in range(n):
                if (j<n-1):           # on fait un swap vers la droite
                    if (0<=i and i<m and 0<=j and j<n-1):
                        voisin = [ligne[:] for ligne in self.state]       #pour ne pas modifier l'état de la grille
                        voisin[i][j],voisin[i][j+1] = voisin[i][j+1],voisin[i][j]  
                        res.append(voisin)

                if (i<m-1):                            # on fait un swap vers le bas
                    if (0<=i and i<m-1 and 0<=j and j<n):
                        voisin = [ligne[:] for ligne in self.state]
                        voisin[i][j],voisin[i+1][j]=voisin[i+1][j],voisin[i][j]
                        res.append(voisin)
        return res

    def adjacent_grid_walls(self):
        m = self.m
        n = self.n
        res = []
        for i in range(m):
            for j in range(n):
                if (j<n-1):           # on fait un swap vers la droite
                    if ((0<=i and i<m and 0<=j and j<n-1)and (all(i1 !=liste_walls_i[index][0] or j1 !=liste_walls_i[index][1] or 
        i2 !=liste_walls_j[index][0] or j2 !=liste_walls_j[index][1] for index in range(len(liste_walls_i)))) and (all(i1 !=liste_walls_j[index][0] or 
        j1 !=liste_walls_j[index][1] or i2 !=liste_walls_i[index][0] or j2 !=liste_walls_i[index][1] for index in range(len(liste_walls_i))))):
                        voisin = [ligne[:] for ligne in self.state]       #pour ne pas modifier l'état de la grille
                        voisin[i][j],voisin[i][j+1] = voisin[i][j+1],voisin[i][j]  
                        res.append(voisin)

                if (i<m-1):                            # on fait un swap vers le bas
                    if ((0<=i and i<m-1 and 0<=j and j<n) and (all(i1 !=liste_walls_i[index][0] or j1 !=liste_walls_i[index][1] or 
        i2 !=liste_walls_j[index][0] or j2 !=liste_walls_j[index][1] for index in range(len(liste_walls_i)))) and (all(i1 !=liste_walls_j[index][0] or 
        j1 !=liste_walls_j[index][1] or i2 !=liste_walls_i[index][0] or j2 !=liste_walls_i[index][1] for index in range(len(liste_walls_i))))):
                        voisin = [ligne[:] for ligne in self.state]
                        voisin[i][j],voisin[i+1][j]=voisin[i+1][j],voisin[i][j]
                        res.append(voisin)
        return res



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

    
    def go_to(self,cell1,cell2):     # on va d'abord a droite(ou a gauche) puis en haut!
        
        (i,j)=cell1        #départ
        (i1,j1)=cell2      #cible
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
'''
test_solution_naive(4,4,[[15,14,13,12],[9,8,7,10],[11,6,5,4],[16,3,2,1]]) 




#grille_test=Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
#print(grille_test.adjacent_grids())

#tests_swap_seq(3,3,[((0,0),(0,1)),((1,2),(1,1))],[[9,8,7],[6,5,4],[3,2,1]])

test_solution_naive(4,4,[[15,14,13,12],[9,8,7,10],[11,6,5,4],[16,3,2,1]])

'''

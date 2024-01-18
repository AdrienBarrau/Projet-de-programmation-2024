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
        # TODO: implement this function (and remove the line "raise NotImplementedError").
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
        # TODO: implement this function (and remove the line "raise NotImplementedError").
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
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        for i in range (len(cell_pair_list)):
            (cell1,cell2)=cell_pair_list[i]
            self.swap(cell1,cell2)

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
    

    
    def get_solveur_hasard(self):
        res=[]
        n=self.n
        m=self.m
        while not(self.is_sorted()):
            print(self.is_sorted())
            self.show()
            
            i=random.randint(0,m-1)
            j=random.randint(0,n-1)
            print((i,j))
            direction=random.randint(0,3)
            if (i==m-1 and j==n-1 and (direction%2==0)):  # coin bas a droite
                self.swap((i,j),(i-1,j))
                res=res+[((i,j),(i-1,j))]
            elif (i==m-1 and j==n-1 and (direction%2==1)):
                self.swap((i,j),(i,j-1))
                res=res+[((i,j),(i,j-1))]
            elif (i==m-1 and j==0 and (direction%2==0)): #coin bas gauche
                self.swap((i,j),(i,j+1))
                res=res+[((i,j),(i,j+1))]
            elif (i==m-1 and j==0 and (direction%2==1)):
                self.swap((i,j),(i-1,j))
                res=res+[((i,j),(i-1,j))]
            elif (i==0 and j==0 and (direction%2==0)):  #coin haut gauche
                self.swap((i,j),(i,j+1))
                res=res+[((i,j),(i,j+1))]
            elif (i==0 and j==0 and (direction%2==1)):
                self.swap((i,j),(i+1,j))
                res=res+[((i,j),(i+1,j))]
            elif (i==0 and j==n-1 and (direction%2==0)): #coin haut droit
                self.swap((i,j),(i-1,j))
                res=res+[((i,j),(i-1,j))]
            elif (i==0 and j==n-1 and (direction%2==1)):
                self.swap((i,j),(i-1,j))
                res=res+[((i,j),(i-1,j))]
            elif (i==0 ): # premiere ligne
                if (direction==0):
                    self.swap((i,j),(i+1,j))
                    res=res+[((i,j),(i+1,j))]
                elif (direction==1):
                    self.swap((i,j),(i,j+1))
                    res=res+[((i,j),(i,j+1))]
                elif (direction==2):
                    self.swap((i,j),(i,j-1))
                    res=res+[((i,j),(i,j-1))]
                
            elif (i==m-1 ): # derniere ligne
                if (direction==0):
                    self.swap((i,j),(i-1,j))
                    res=res+[((i,j),(i-1,j))]
                elif (direction==1):
                    self.swap((i,j),(i,j+1))
                    res=res+[((i,j),(i,j+1))]
                elif(direction==2):
                    self.swap((i,j),(i,j-1))
                    res=res+[((i,j),(i,j-1))]
            elif (j==0 ): #1ere colonne
                if (direction==0):
                    self.swap((i,j),(i+1,j))
                    res=res+[((i,j),(i+1,j))]
                elif (direction==1):
                    self.swap((i,j),(i-1,j))
                    res=res+[((i,j),(i-1,j))]
                elif(direction==2):
                    self.swap((i,j),(i,j+1))
                    res=res+[((i,j),(i,j+1))]
            
            elif (j==n-1): #derniere colonne
                if (direction==0):
                    self.swap((i,j),(i+1,j))
                    res=res+[((i,j),(i+1,j))]
                elif (direction==1):
                    self.swap((i,j),(i-1,j))
                    res=res+[((i,j),(i-1,j))]
                elif (direction==2):
                    self.swap((i,j),(i,j-1))
                    res=res+[((i,j),(i,j-1))]
            else:        #cas general
                if (direction==0):
                    self.swap((i,j),(i,j+1))
                    res=res+[((i,j),(i,j+1))]
                elif (direction==1):
                    self.swap((i,j),(i-1,j))
                    res=res+[((i,j),(i-1,j))]
                elif(direction==2):
                    self.swap((i,j),(i,j+1))
                    res=res+[((i,j),(i,j+1))]
                elif(direction==3):
                    self.swap((i,j),(i+1,j))
                    res=res+[((i,j),(i+1,j))]
        self.show()
        return res



    def get_solution_naive(self):
        """
        Solves the grid and returns the sequence of self.s at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        m=self.m 
        n=self.n
        res=[]
        for i in range(m-1):
            for j in range(n-1):
                if (self.is_sorted()):
                    return res
                elif:
                    (i==m-1 and j==n-1 ):  # coin bas a droite
                        if (self.state[i][j]>self.state[i][j-1]):
                            self.swap((i,j),(i,j-1))
                            res=res+[((i,j),(i,j-1))]
                        if (self.state[i][j]>self.state[i][j-1]):
                            self.swap((i,j),(i-1,j))
                            res=res+[((i,j),(i-1,j))]
                elif:
                    (i==n-1):
                        if (self.state[i][j]>self.state[i][j+1]):
                            self.swap((i,j),(i,j+1))
                            res=res+[((i,j),(i,j+1))]
                elif:
                    (j==n-1):
                        if (self.state[i][j]>self.state[i+1][j]):
                            self.swap((i,j),(i+1,j))
                            res=res+[((i,j),(i+1,j))]    
                elif:
                    

def tests_swap(m,n,i1,j1,i2,j2,state):

    Grille_ex=Grid(m,n,state)
    Grille_ex.show()
    Grille_ex.swap((i1,j1),(i2,j2))
    Grille_ex.show()
  
def tests_swap_seq(m,n,liste_swap,state):

    Grille_ex=Grid(m,n,state)
    Grille_ex.show()
    Grille_ex.swap_seq(liste_swap)
    Grille_ex.show()

def test_hasard(m,n,state):

    Grille_ex2=Grid(m,n,state)
    print(len(Grille_ex2.get_solveur_hasard()))


#test_hasard(2,4,[[8,6,5,4],[7,3,2,1]])   37877 operations

#tests_swap_seq(3,3,[((0,0),(0,1)),((1,2),(1,1))],[[9,8,7],[6,5,4],[3,2,1]])


"""
This is the graph module. It contains a minimalistic Graph class.
"""
#Test commit

from grid import Grid
import time

def tuple_into_matrice(tup):
    return [[tup[i][j] for j in range (len(tup[0])) ]for i in range (len(tup)) ]

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs(self, src, dst): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        seen = set()  # tableau des vues
        to_explore = [src]
        dict_pere={src: None}     #une liste n'aurai pas permit d acceder a un element du type liste_pere[v] avec v un tuple
        while not (to_explore==[]):
            noeud_cur = to_explore.pop(0)
            if (noeud_cur == dst):
                
                chemin = [noeud_cur]
                while dict_pere[noeud_cur] is not src:
                    noeud_cur = dict_pere[noeud_cur]
                    if not (noeud_cur in chemin):  # Vérifier si le noeud a déjà été visité lors de la reconstitution

                        chemin.append(noeud_cur)
                chemin.append(src)
                chemin.reverse()
                return chemin

            voisins = self.graph[noeud_cur]
            for v in voisins:
                if v not in seen:
                    seen.add(v)
                    dict_pere[v] = noeud_cur
                    to_explore.append(v)

        return None

    def new_bfs(self, src, dst):     #on fait le graph au fur et à mesure
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        seen = set()  # tableau des vues, on utilise un set() car aucun ordre n'est requis
        to_explore = [src]
        dict_pere={src: None}     #une liste n'aurai pas permit d acceder a un element du type liste_pere[v] avec v un tuple
        while not (to_explore==[]):
            noeud_cur = to_explore.pop(0)
            print(noeud_cur)

            if (noeud_cur == dst):
               
                chemin = [noeud_cur]
               
                while dict_pere[noeud_cur] is not src:
                    noeud_cur = dict_pere[noeud_cur]
                    if not (noeud_cur in chemin):  # Vérifier si le noeud a déjà été visité lors de la reconstitution

                        chemin.append(noeud_cur)
                
                chemin.append(src)
                chemin.reverse()
                
                return chemin

            grille_init = Grid(len(src),len(src[0]),tuple_into_matrice(noeud_cur))
            voisins=[]
            
            for grille in grille_init.adjacent_grids():
                new=Graph.matrice_into_tuple(grille)
                if new not in self.nodes:
                    self.nodes=self.nodes+[new]
                    voisins=self.nodes
                    
            for v in voisins:
                if v not in seen:
                    seen.add(v)
                    dict_pere[v] = noeud_cur
                   
                    to_explore.append(v)
                    

        return None





    @classmethod

    def distance_heuristique(node) : #renvoi la distance a la solution, en somment la distance a vol d'oiseua entre chaque coefficients
        mat=tuple_into_matrice(node)
        m=len(node)
        n=len(node[0])
        res=0   #resultat
        for i in range (m):
            for j in range(n):
                k=mat[i][j]
                i1=int((k-1)/n)  #!i1 et j1 sont les coordonees de la valeur k dans la grille solution!

                j1=(k-1)%n 

                res=res+sqrt((i-i1)**2+(j-j1)**2)
        return res

    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph






    def generate_matrices(m,n):   #renvoi la liste de (m*n)! matrices de taille m*n
    
        res=[]   #tableau de matrices
        def generate_permutations(mat, cur):
            if (len(cur)== m*n):    #si len(cur)=m*n on a remplie une permetutation en entier         
                res.append([cur[i:i+n] for i in range(0,len(cur),n)] ) 
            else:
                for i in range(len(mat)):
                    ind = mat[i]
                    m2 = mat[:i] + mat[i+1:]
                    generate_permutations(m2, cur + [ind])
    
        
        generate_permutations([i for i in range(1,m*n+1)], [])
    
        return res

    def matrice_into_tuple(mat):    # conversion de matrice en tuple
        return tuple(tuple(i) for i in mat)

    def generate_graph(m,n):  # Initialisa le graphe avec (m*n)! de type hashable, d'ou l'utilisation des tuples
        matrices = Graph.generate_matrices(m,n)
        nodes = [Graph.matrice_into_tuple(mat) for mat in matrices]
        graph = Graph(nodes)     #initialisation du graph avec une liste de tout les etats possible (les tuples sont non mutables)

        for mat in matrices:
            grid = Grid(m,n,mat)
            mat_tuple = Graph.matrice_into_tuple(mat)
            for adjacent_matrice in grid.adjacent_grids():
                graph.add_edge(mat_tuple, Graph.matrice_into_tuple(adjacent_matrice))

        return graph

    def solve_bfs(grille):  
        m=grille.m
        n=grille.n
        all_states_graph=(Graph.generate_graph(m,n))
        return all_states_graph.bfs(Graph.matrice_into_tuple(grille.state),Graph.matrice_into_tuple([[i*m+j+1 for j in range (n)] for i in range (m)]))          # l'etat initial self est la source, la grille triee est la destination

    def solve_new_bfs(grille):
        m=grille.m
        n=grille.n
        x=Graph([])
        return x.new_bfs(Graph.matrice_into_tuple(grille.state),Graph.matrice_into_tuple([[i*m+j+1 for j in range (n)] for i in range (m)]))


"""
début d'essai de la fonction A* ( Diane)

def distance(start,goal):
    N=0 # initialisation du nombre de noeuds pour arriver à la destination
    # à continuer, poser des questions à partir de bfs ? est-ce qu'on peut faire avec ça ???

def chemin_a(start, goal):
    to_explore = []
    seen = []
    to_explore.append(start)
    seen.append(start)
    next = start
    current_d = -1
    while next!= goal:
        neighbours = graph[to_explore[0]] # là pas le bon nom de fonction mais je cherche après 
        for n in neighbours:
            to_explore.append(n)
        to_explore.del(0) # voir pourquoi ya erreur ici et pas plus tard en plus quand je réutilise del?
        while to_explore != []:
            new_d = distance(to_explore[0], goal) # fonction pas encore définie
            if new_d < current_d or current_d==-1 :
                current_d = new_d
                next = to_explore[0]
            to_explore.del(0)
        seen.append(next)
        to_explore.append(next)
    return seen


idee fonction distance: renvoi la somme des ecarts pour chaque coordonnee, cette dist surestime
la vrai distance, peut etre faire pareil avec dist a vol d'oiseau.
"""

graphe_ex=Graph ([1,2,3,4,5,6])
graphe_ex.add_edge(1,2)
graphe_ex.add_edge(2,3)
print(graphe_ex)
print(graphe_ex.bfs(1,3))
graphe_ex.add_edge(1,3)
print(graphe_ex.bfs(1,3))

graphe_ex.add_edge(3,4)
graphe_ex.add_edge(4,5)
graphe_ex.add_edge(5,6)
graphe_ex.add_edge(2,6)
print(graphe_ex)
print(graphe_ex.bfs(1,6))

graphe_test=Graph.graph_from_file("input/graph1.in")
print(graphe_test.bfs(5,14))
print(graphe_test.bfs(3,15))
print(graphe_test.bfs(2,16))


#print(Graph.generate_matrices(2,2))
#print(Graph.generate_graph(2,2))
grille3=Grid(3,3,[[9,8,7],[6,5,4],[3,2,1]])

deb1=time.time()
print(Graph.solve_bfs(grille3))
fin1=time.time()
print(fin1-deb1)
deb2=time.time()
print(Graph.solve_new_bfs(grille3))
fin2=time.time()
print(fin2-deb2)

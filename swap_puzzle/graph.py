"""
This is the graph module. It contains a minimalistic Graph class.
"""
#Test commit

from grid import Grid



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
        seen=[src]                          # on fait un tableau qui contient les noeuds visités
        to_explore=[src] 
        tableau_pere=[[src] for i in range (self.nb_nodes+1)]                #tableau de tableau qui contiennent les ancetres des noeuds(pour pouvoir reconstituer le parcours)                 
        while not (to_explore==[]):
            noeud_cur=to_explore[0]
            if (noeud_cur==dst):
                                                                     #on inclu la destination dans le parcours d'ancetres
                tableau_pere[noeud_cur].append(dst)
                return tableau_pere[noeud_cur]

            else:
                voisins=self.graph[noeud_cur]
                for v in (voisins):
                    if not(v in seen):
                        seen.append(v)
                        if not (noeud_cur in tableau_pere[v]):        
                            tableau_pere[v].append(noeud_cur)
                        to_explore.append(v)
                del(to_explore[0])
        return None

    @classmethod
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


    def generate_matrices(m,n):
    
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

    def generate_graph(m,n):
        graph=Graph(Graph.generate_matrices)

        
    def solve_bfs(grille):
        m=grille.m
        n=grille.n
        all_states_graph=Graph(Graph.generate_matrices(m,n))
        return bfs(all_states_graph,grille.state,[[i*m+j+1 for j in range (n)] for i in range (m)])          # l'etat initial self est la source, la grille triee est la destination


# idee: associer a chaque noeud(etat de la grille) une position dans un espace de dimension le nombre de swaps possibles

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

graphe_test=Graph.graph_from_file('graph1.in')
print(graphe_test.bfs(5,14))
print(graphe_test.bfs(3,15))
print(graphe_test.bfs(2,16))



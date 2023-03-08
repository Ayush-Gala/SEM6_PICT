import networkx as nx
import matplotlib.pyplot as plt

'''
Class that will help in graph visualization
'''
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


'''
Actual implementation of Graph Data Structure
'''
class Graph:
  
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = [] # to store graph
        self.visual = []
  
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
  
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
          # Reassignment of node's parent to root node as
          # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]
  
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
  
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
  
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
  
    # The main function to construct MST using Kruskal's
        # algorithm

    def visualizestart(self):
        G = nx.Graph()
        G.add_weighted_edges_from(self.graph, weight='weight')
        nx.draw_networkx(G)
        plt.show()

    def visualize(self):
        G = nx.Graph()
        G.add_weighted_edges_from(self.visual, weight='weight')
        # pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G)
        # labels = nx.get_edge_attributes(G,'weight')
        # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()

    def KruskalMST(self):

        result = []  # This will store the resultant MST
  
        # An index variable, used for sorted edges
        i = 0
  
        # An index variable, used for result[]
        e = 0
  
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
  
        parent = []
        rank = []
  
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
  
        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:
  
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
  
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.visual.append([u,v,w])
                self.union(parent, rank, x, y)
            # Else discard the edge
  
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
  
if __name__ == '__main__':

    #start of Menu Driven program
    g = Graph(int(input("How many vertices are there in the graph: ")))
    while(True):
        choice = int(input("1. Add a new edge. \n2. Execute Kruskals\n-1 to EXIT. \nYour choice: "))
        if choice == 1:
            s = int(input("Starting vertice: "))
            e = int(input("Ending vertice: "))
            w = int(input("Weight of edge: "))
            g.addEdge(s,e,w)

        elif choice == 2:
            g.visualizestart()
            g.KruskalMST()
            g.visualize()
        else:
            break
        
    print("Thank you so much!")


'''
Test Input Sequence 1:

7
1
0
1
7
1
0
3
5
1
3
1
9
1
3
4
15
1
3
5
6
1
1
2
8
1
1
4
7
1
5
4
8
1
5
6
11
1
2
4
5
1
4
6
9
2

'''
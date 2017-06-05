import Graph
import random

class SmallWorldGraph(Graph.Graph):

    def rewire(self, p):
        "Probabilistically rewires the edges in the graph to produce a Watts-Strogatz model of a small-world graph"
        #Start from ring lattice
        vertices = self.vertices()
        numVertices = len(vertices)

        #Get degree of vertices
        k = len(self[vertices[0]])
        numLoops = k/2

        #We have k/2 total loops. Within each loop, we loop over all nodes and probabilistically rewire an edge
        for i in range(k/2):

            #Loop over all nodes
            for index in range(numVertices):

                #Check link to (i+1)th nearest neighbour in clockwise direction, and probabilistically rewire it
                neighbourIndex = (index + i + 1) % numVertices

                #Get edge between current node and its (i+1)th nearest neighbour in clockwise direction
                e = self.get_edge(vertices[index], vertices[neighbourIndex])

                #Determine whether or not it will be rewired
                if(random.random() <= p):
                    #It's getting rewired. Pick a node to move the edge to, disallowing duplicate edges and loops
                    self.remove_edge(e) #Remove old edge
                    found = False
                    targetIndex = 0
                    #Find vertex for new edge
                    while(not found):
                        targetIndex = random.randint(0,numVertices-1)
                        if (targetIndex != index and targetIndex != neighbourIndex):
                            #It's not a loop. Make sure it isn't a duplicate
                            eCheck = self.get_edge(vertices[index], vertices[targetIndex])
                            if(eCheck == False):
                                found = True #Not a duplicate
                        if(found):
                            #We've found the new node. Rewire the edge by removing the old edge and adding a new one
                            newEdge = Graph.Edge(vertices[index], vertices[targetIndex])
                            self.add_edge(newEdge) #Add new edge

                else:
                    #Leave it be
                    pass

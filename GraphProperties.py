import Graph
import RandomGraph
from collections import deque

def BFS(g, source, goal):
    #Use BFS to find shortest path length
    numVisited = 0
    #Set up visited and previous dictionaries
    visited = {}
    prev = {}
    for key in g:
        visited[key] = False
        prev[key] = None
    #Set up queue
    q = deque([source])
    #Search graph
    while(len(q)!=0 and not visited[goal]):
        #Pop head of queue
        curNode = q.popleft()
        #Mark node as visited
        visited[curNode] = True
        numVisited = numVisited + 1
        #Search all adjacent nodes
        neighbours = g.out_vertices(curNode)
        for neighbour in neighbours:
            if(visited[neighbour] == False and not (neighbour in q)):
                #Add neighbour to q if it's unvisited, and not already in q
                q.append(neighbour)
                prev[neighbour] = curNode

    #Determine path from source to goal (start at goal and trace back parents to source)
    if(visited[goal]):
        path = []
        path.append(goal)
        parent = prev[goal]
        while(parent != None):
            path.append(parent)
            parent = prev[parent]
        return len(path)
    else:
        return -1

def characteristicPathLength(graph):
    #Find all pairs of vertices
    vertices = graph.vertices()
    pairs = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            source = vertices[i]
            dest = vertices[j]
            pair = (source, dest)
            pairs.append(pair)
    #Calculate all path lengths
    sumOfPathLengths = 0
    for pair in pairs:
        dist = BFS(graph, pair[0], pair[1])
        sumOfPathLengths = sumOfPathLengths + dist
    #Calculate and return average
    avg = float(sumOfPathLengths/len(pairs))
    return avg

def getNumEdges(g, nodeSet):
    #Given a graph, and a subset of nodes from the graph, calculate the number of edges between them
    numEdges = 0
    for i in range(len(nodeSet)):
        for j in range(i+1, len(nodeSet)):
            #Check if there is an edge between these two nodes
            e = g.get_edge(nodeSet[i], nodeSet[j])
            if(e):
                numEdges = numEdges + 1
    return numEdges

def clusteringCoefficient(g):
    #Retrieve all nodes of graph
    nodes = g.vertices()
    sumOfCoefficients = float(0.0)

    #Calculate each nodes clustering coefficient
    for node in nodes:
        #Get all of the nodes neighbours
        neighbours = g.out_vertices(node)
        #Calculate the maximum number of edges that can exist between all of the neighbours
        maxNumEdges = float(float(len(neighbours))*float((len(neighbours)-1)/float(2.0)))
        #Calculate the number of edges that actually exist between them
        numActualEdges = getNumEdges(g, neighbours)
        #Calculate the coefficient
        nodeCoefficient = 0.0
        if(maxNumEdges != 0):
            nodeCoefficient = float(numActualEdges/maxNumEdges)
        sumOfCoefficients = float(float(sumOfCoefficients) + float(nodeCoefficient))

    #Calculate the clustering coefficient of the graph
    coefficient = float(float(sumOfCoefficients)/float(len(nodes)))
    return coefficient

def simulation():
    #Make regular graph of degree 4, 100 nodes
    g = Graph.Graph()
    for i in range(1,101):
        g.add_vertex(i)
    g.add_regular_edges(4)

    #Make random graph with p=0.15, 100 nodes
    rg = RandomGraph.RandomGraph()
    for i in range(1,101):
        rg.add_vertex(i)
    rg.add_random_edges(0.15)

    #Evalute clustering coefficient and characteristic path length for each
    gPathLength = characteristicPathLength(g)
    rgPathLength = characteristicPathLength(rg)

    gClusteringCoefficient = clusteringCoefficient(g)
    rgClusteringCoefficient = clusteringCoefficient(rg)

    print('Regular graph: ', gPathLength, gClusteringCoefficient)
    print('Random graph: ', rgPathLength, rgClusteringCoefficient)

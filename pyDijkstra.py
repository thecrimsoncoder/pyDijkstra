from collections import defaultdict
from heapq import *

print("+-------------------------------------+")
print("|     p y D I J K S T R A . P Y       |")
print("| By: Sean McElhare (TheCrimsonCoder) |")
print("+-------------------------------------+")


def buildEdges():
    edges = list()
    numEdges = input("How many edges would you like to create?: ")
    for x in range(int(numEdges)):

        startNode = input("Please enter a STARTING NODE for this EDGE: ")
        endNode = input("Please enter a ENDING NODE for this EDGE: ")
        linkCost = input("And what is the link cost between " + str(startNode) + " and " + str(endNode) + " :")

        edge = (startNode,endNode,int(linkCost))
        edges.append(edge)

    return edges

def findPaths(edges):
    for edge in edges:
        return dijkstra(edges,edge[0],edge[1])

def buildTableHeader(startingNodes):
    startingNodes.remove(startingNodes[0])
    headerString = "     Add to S"
    for node in startingNodes:
        headerString = headerString + "     " + node

    return headerString

def dijkstra(edges, startNode, endNode):
    g = defaultdict(list)
    for startingNodeListValue, endingNodeListValue, linkCostListValue in edges:
        g[startingNodeListValue].append((linkCostListValue, endingNodeListValue))

    pathList = [(0, startNode, ())]
    visitedNodes = set()

    while pathList:
        (cost, v1, path) = heappop(pathList)
        if v1 not in visitedNodes:
            visitedNodes.add(v1)
            path = (v1, path)
            if v1 == endNode:
                return (cost, path)

            for linkCostListValue, v2 in g.get(v1, ()):
                if v2 not in visitedNodes:
                    heappush(pathList, (cost + linkCostListValue, v2, path))

    return float("∞")

def buildStartingNodesList(edges):
    startingNodesDict = defaultdict(list)
    for startingNode, endingNode, linkCost in edges:
        startingNodesDict[startingNode].append(linkCost)

    startingNodes = list()
    for nodes in startingNodesDict:
        startingNodes.append(nodes[0])

    return startingNodes

def buildEndingNodesList(edges):
    endingNodesDict = defaultdict(list)
    for startingNode, endingNode, linkCost in edges:
        endingNodesDict[endingNode].append(linkCost)

    endingNodes = list()
    for nodes in endingNodesDict:
        endingNodes.append(nodes[0])

    return endingNodes


def printList(list):
    for element in list:
        print(element)

def main():
    # UNCOMMENT FOR FINAL VERSION!!!
    #edges = buildEdges()
    edges = [
                 ('A','B',32),
                 ('B','C',3242),
                 ('C','D',23),
                 ('D','E',1231),
                 ('E','F',3242),
                 ('F','G',2123),
                 ('H','I',4353),
                 ('I','J',324),
                 ('Z','A',32242),
                 ('B','E',342),
                 ('Z','C',324),
                 ('K','L',23),
                 ('L','Q',3242)
            ]
    startingNodes = buildStartingNodesList(edges)
    endingNodes = buildEndingNodesList(edges)

    print("Graph Data: ")
    printList(edges)
    print("\n")
    print("Dijkstra's Shortest Path: \n")
    print(buildTableHeader(startingNodes))
    print("===========================================================================================================")
    for startingNode in startingNodes:
        for endingNode in endingNodes:
            print(dijkstra(edges,startingNode,endingNode))
    print("===========================================================================================================")



main()

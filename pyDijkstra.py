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

def printOutput():
    return True

def dijkstra(edges, startNode, endNode):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q = [(0, startNode, ())]
    visitedNodes = set()

    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in visitedNodes:
            visitedNodes.add(v1)
            path = (v1, path)
            if v1 == endNode:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in visitedNodes:
                    heappush(q, (cost + c, v2, path))

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

    edges = buildEdges()
    print("Starting Nodes:")
    startingNodes = buildStartingNodesList(edges)
    print("Ending Nodes: ")
    endingNodes = buildEndingNodesList(edges)

    for startingNode in startingNodes:
        for endingNode in endingNodes:
            print(">> Computing path" + startingNode + " to " + endingNode)
            print(dijkstra(edges,startingNode,endingNode))

main()

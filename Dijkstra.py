from .MinHeap import *
import sys


class Dijkstra:
    def __init__(self):
        self.heap = None    # initialization for MinHeap with empty list of vertices
        self.graph = None
        self.destination = None
        self.source = None
        pass

    def dijkstra(self):

        self.initializeSingleSource()
        S = []                   # a set of vertices whose final shortest path weights have already been determined
        Q = list(self.graph.vertexMap.values())                         # list of vertices
        self.heap = MinHeap(Q, key=lambda vertex: vertex.d)             # heap implementation using key as vertex.

        # while Q != None and len(Q) > 0:
        #     minDVertex = min(Q, key= lambda  v: v.d)  # If using basic list, which uses O(n) as the running time.
        #     Q.remove(minDVertex)

        while len(self.heap) > 0:
            minDVertex = self.heap.extractMin()
            if not minDVertex.status :
                continue                                                # skipping the vertices which are down.
            S.append(minDVertex)
            for edge in minDVertex.adj:                                 # retrieving edges
                # print("adjacent item is ", edge.destination.name)
                if not edge.status or not edge.destination.status:
                    continue                                            # skipping the edges which are down.
                nextVertex = edge.destination                           # retrieving destination vertex from edge data
                transit_time = edge.transit_time
                self.Relax(minDVertex, nextVertex, transit_time)

        return self.source, self.destination

    def Relax(self, minDVertex, nextVertex, transit_time):
        newValue = minDVertex.d + transit_time
        if nextVertex.d > newValue:
            # nextVertex.d = minDVertex.d + transit_time
            self.heap.heapDecreaseKey(nextVertex, newValue, nextVertex.setKeyForHeap)
            nextVertex.pi = minDVertex

    def initializeSingleSource(self):                       # O(V)
        for vertex in self.graph.vertexMap.values():
            vertex.d = sys.maxsize
            vertex.pi = None
        self.source.d = 0

    def minPath(self, graph, source, destination, return_list=True):
        self.graph = graph
        self.destination = graph.vertexMap[destination]
        self.source = graph.vertexMap[source]               #O(1)

        if return_list:
            path = []

            def traverse(source_inner, destination_inner):
                if destination_inner == source_inner:
                    path.append(destination_inner.name)
                elif destination_inner.pi is None:
                    return
                else:
                    traverse(source_inner, destination_inner.pi)
                    path.append(destination_inner.name)

            self.dijkstra()
            traverse(self.source, self.destination)
            return path
        else:
            return self.dijkstra()

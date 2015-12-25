from .Vertex import *
from .Edge import *
import math


class Graph:

    def __init__(self):
        self.vertexMap = {}

    def addEdge(self, sourceName, destinationName, transit_time):
        source = self.getVertex(sourceName, createNew=True)
        destination = self.getVertex(destinationName, createNew=True)
        source.addEdge(Edges(source, destination, float(transit_time)))
        destination.addEdge(Edges(destination, source, float(transit_time)))

    def updateEdge(self, source, destination, transit_time):
        s = self.getVertex(source, createNew=True)
        d = self.getVertex(destination, createNew=True)
        edge = s.getEdgeFromVertex(d)
        if edge is not None:
            edge.transit_time = float(transit_time)
        else:
            s.addEdge(Edges(s, d, float(transit_time)))

    def deleteEdge(self, source, destination):
        s = self.getVertex(source)
        d = self.getVertex(destination)
        if s is None and d is None:
            print("%s and %s vertices not present" % (source, destination))
        elif s is None:
            print("%s vertex not present" % source)
        elif d is None:
            print("%s vertex not present" % destination)
        else:
            s.deleteEdge(d)

    def upEdgeStatus(self, sourceName, destinationName):
        s = self.getVertex(sourceName)
        d = self.getVertex(destinationName)
        if s is None and d is None:
            print("%s and %s vertices not present" %(sourceName, destinationName))
        elif s is None:
            print("%s vertex not present" % sourceName)
        elif d is None:
            print("%s vertex not present" % destinationName)
        else:
            edge = s.getEdgeFromVertex(d)
            if edge is not None:
                if not edge.status:
                    edge.status = not edge.status
                else:
                    print("Edge from %s to %s is already Up" % (sourceName, destinationName))
            else:
                print("Edge from %s to %s is not present" % (sourceName, destinationName))

    def downEdgeStatus(self, sourceName, destinationName):
        s = self.getVertex(sourceName)
        d = self.getVertex(destinationName)
        if s is None and d is None:
            print("%s and %s vertices not present" % (sourceName, destinationName))
        elif s is None:
            print("%s vertex not present" % sourceName)
        elif d is None:
            print("%s vertex not present" % destinationName)
        else:
            edge = s.getEdgeFromVertex(d)
            if edge is not None:
                if edge.status:
                    edge.status = not edge.status
                else:
                    print("Edge from %s to %s is already Down" % (sourceName, destinationName))
            else:
                print("Edge from %s to %s is not present" % (sourceName, destinationName))

    def upVertexStatus(self, _vertex):
        s = self.getVertex(_vertex)
        if s is None:
            print("Vertex %s is not present" % _vertex)
        else:
            if not s.status:
                s.status = not s.status
            else:
                print("Vertex %s is already Up" % _vertex)

    def downVertexStatus(self, _vertex):
        s = self.getVertex(_vertex)
        if s is None:
            print("Vertex %s is not present" % _vertex)
        else:
            if s.status:
                s.status = not s.status
            else:
                print("Vertex is already down")

    def getVertex(self, vertexName, createNew=False):
        try:
            v = self.vertexMap.get(vertexName)
            if v is None and createNew:
                v = Vertex(vertexName)
                self.vertexMap[vertexName] = v
            return v
        except KeyError as e:
            print("Exception ", e)

    def addVertex(self, vertexName):
        self.getVertex(vertexName, createNew=True)

    def get_all_vertices_name(self):
        return list(self.vertexMap.keys())

    def __len__(self):
        return len(self.vertexMap)

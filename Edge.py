class Edges:

    """define from and to vertex"""

    def __init__(self, source, destination, transit_time):
        self.status = True
        self.source = source
        self.destination = destination
        self.transit_time = transit_time

    def setTransitTime(self, transit_time):
        self.transit_time = transit_time
        return True

    def __repr__(self):
        return "Edge data \nstatus : %s source : %s destination : %s transit_time : %s"\
               % (self.status, self.source, self.destination, self.transit_time)

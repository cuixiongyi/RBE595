class binID:
    def __init__(self, x, y):
        self.binX = x
        self.binY = y

class SimpleMapBin:

    def __init__(self, x0, y0, idX, idY):
        self.x0 = x0
        self.y0 = y0
        self.id = binID(idX, idY)
        self.isObstacle = None
        self.G = 0
        self.H = 0
        self.parent = None

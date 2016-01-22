import ThreeDOF
from LineSegment import *
import matplotlib.pyplot as plt
__author__ = 'xiongyi'

obstaclesStyle = '-b'

class SimulatorUtility:
    def __init__(self, sim):
        self.figure, self.ax = plt.subplots()
        self.lines = self.ax.plot([],[], '-')
        self.ax.set_xlim(self.width, self.height)


    def initObstacles(self, sim):

        obstacle = []
        obstacle.append(LineSegment(0,0,0,sim.height))
        obstacle.append(LineSegment(0,sim.height,sim.width,sim.height))
        obstacle.append(LineSegment(sim.width,sim.height,sim.width,0))
        obstacle.append(LineSegment(sim.width,0,0,0))

        obstacle.append(LineSegment(100, 100, 100, 50))
        obstacle.append(LineSegment(100, 50, 50, 50))
        obstacle.append(LineSegment(50, 50, 50, 100))
        obstacle.append(LineSegment(50, 100, 100, 100))

        return obstacle


    def drawLine(self, lineSeg, style):
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        plt.plot([lineSeg.sx,lineSeg.ex], [lineSeg.sy, lineSeg.ey], style)

    def drawSimulator(self, sim):

        for line in sim.obstacle:
            SimulatorUtility.drawLine(line, obstaclesStyle)
        import threading
        t = threading.Thread(plt.show())
        t.start()




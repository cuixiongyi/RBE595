__author__ = 'xiongyi'
import random
import threading


from DataType import ThreeDOF, Coordinate
from Simulator import *
from Simulator.SimulatorMeasure import *
from Simulator.SimulatorUtility import *
from Simulator.Geometry.LineSegment import *
from Navigation.Astar  import *
from Navigation.Map  import *

class Simulator(threading.Thread):

    def __init__(self, f, canvas):
        self.fig = f
        self.canvas = canvas
        self.pathTrackOn = True;
        self.height = 400
        self.width = 600
        self.x0 = 0
        self.y0 = 0
        self.x1 = self.x0 + self.width
        self.y1 = self.y0 + self.height
        self.time = 0.0
        self.TIMEINC = 0.1
        self.robotDOF = ThreeDOF.ThreeDOF()
        self.robotDOF.xy.x = 1
        self.robotDOF.xy.y = 1
        self.utility = SimulatorUtility(self)
        self.inputMove = ThreeDOF.ThreeDOF()
        self.obstacles = self.utility.initObstacles(self)
        self.measureDists = []
        self.measureHits = []
        self.goal = Coordinate.Coordinate(400, 250)
        self.map = Map(self)
        self.astar = Astar(self, self.map)
        path = self.astar.calculate(self.robotDOF.xy, self.goal)
        self.astarPathX = []
        self.astarPathY = []
        # print('path = ', path)
        for p in path:
            self.astarPathX.append(p.x0)
            self.astarPathY.append(p.y0)
        self.pathCount = 0


    def run(self):
        print('\n\n')
        print('robot xy = ', self.robotDOF.xy.x, self.robotDOF.xy.y, self.robotDOF.theta)


        self.time += self.TIMEINC
        moveStep = 7
        # self.inputMove.xy.x = random.uniform(0,moveStep)
        # self.inputMove.xy.y = random.uniform(0,moveStep)
        self.inputMove.xy.x = self.astarPathX[self.pathCount] - self.robotDOF.xy.x
        self.inputMove.xy.y = self.astarPathY[self.pathCount] - self.robotDOF.xy.y
        self.pathCount += 1
        self.moveTo(self.inputMove)
        SimulatorMeasure.measure(self)
        # print(self.measureDists)
        self.utility.drawSimulator(self)
        self.canvas.draw()
        self.canvas.flush_events()
        # self.canvas.show()
        return True

    def TurnOnOffPathTrack(self, withPathTrack):
        if (withPathTrack):
            self.pathTrackOn = True
        else:
            self.pathTrackOn = False

    def moveTo(self, inputMoveDOF):
        lineMovement = LineSegment.LineSegment(self.robotDOF.xy.x,
                                               self.robotDOF.xy.y,
                                               self.robotDOF.xy.x+inputMoveDOF.xy.x,
                                               self.robotDOF.xy.y+inputMoveDOF.xy.y)

        if Simulator.checkMovement(self.obstacles, lineMovement):
        # if True:
            self.robotDOF.xy.x = lineMovement.ex
            self.robotDOF.xy.y = lineMovement.ey
            self.robotDOF.xy.theta = self.robotDOF.theta + inputMoveDOF.theta
            return True
        else:
            return False

    # inpute relative translation
    @staticmethod
    def checkMovement(obstacles, lineMovement):
        for obs in obstacles:
            ret = obs.checkLineSegCross(lineMovement)
            # print(ret)
            if ret is not None:
                # print(ret)
                return False
        else:
            return True


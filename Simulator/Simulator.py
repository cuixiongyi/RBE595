__author__ = 'xiongyi'
import random
import threading

import Simulator.SimulatorMeasure

from DataType import ThreeDOF, Coordinate
from Simulator import SimulatorUtility
from Simulator import SimulatorMeasure
from Simulator.Geometry.LineSegment import *


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
        self.utility = SimulatorUtility.SimulatorUtility(self)
        self.inputMove = ThreeDOF.ThreeDOF()
        self.obstacles = self.utility.initObstacles(self)
        self.measureDists = []
        self.measureHits = []
        self.goal = Coordinate.Coordinate(400, 250)



    def run(self):
        print('\n\n\n\n\n')
        print('robot xy = ', self.robotDOF.xy.x, self.robotDOF.xy.y, self.robotDOF.theta)

        self.time += self.TIMEINC
        moveStep = 7
        self.inputMove.xy.x = random.uniform(0,moveStep)
        self.inputMove.xy.y = random.uniform(0,moveStep)
        self.moveTo(self.inputMove)
        SimulatorMeasure.SimulatorMeasure.measure(self)
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
        lineMovement = LineSegment(self.robotDOF.xy.x,
                                               self.robotDOF.xy.y,
                                               self.robotDOF.xy.x+inputMoveDOF.xy.x,
                                               self.robotDOF.xy.y+inputMoveDOF.xy.y)

        if self.checkMovement(lineMovement):
        # if True:
            self.robotDOF.xy.x = lineMovement.ex
            self.robotDOF.xy.y = lineMovement.ey
            self.robotDOF.xy.theta = self.robotDOF.theta + inputMoveDOF.theta
            return True
        else:
            return False

    # inpute relative translation
    def checkMovement(self, lineMovement):
        for obs in self.obstacles:
            ret = obs.checkLineSegCross(lineMovement)
            # print(ret)
            if ret is not None:
                print(ret)
                return False
        else:
            return True


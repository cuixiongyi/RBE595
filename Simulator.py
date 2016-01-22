__author__ = 'xiongyi'
import ThreeDOF
from LineSegment import *
import SimulatorUtility
import threading
import tkinter as tk

class Simulator(threading.Thread):

    def __init__(self, f, canvas):
        self.fig = f
        self.canvas = canvas
        self.pathTrackOn = True;
        self.height = 400
        self.width = 600
        self.time = 0.0
        self.TIMEINC = 0.1
        self.robotDOF = ThreeDOF.ThreeDOF()
        self.utility = SimulatorUtility.SimulatorUtility(self)
        self.obstacles = self.utility.initObstacles(self)
        # threading.Thread.run()


    def run(self):
        self.time += self.TIMEINC
        print(self.robotDOF.xy.x, self.robotDOF.xy.y, self.robotDOF.theta)
        self.utility.drawSimulator(self);
        self.canvas.draw()
        self.canvas.flush_events()
        self.canvas.show()
        return True

    def TurnOnOffPathTrack(self, withPathTrack):
        if (withPathTrack):
            self.pathTrackOn = True
        else:
            self.pathTrackOn = False

    def moveTo(self, inputDOF):
        lineMovement = LineSegment.LineSegment(self.robotDOF.xy.x,
                                               self.robotDOF.xy.y,
                                               inputDOF.xy.x,
                                               inputDOF.xy.y)

        if self.checkMovement(lineMovement):
            self.robotDOF.xy.x = self.robotDOF.xy.x + inputDOF.xy.x
            self.robotDOF.xy.y = self.robotDOF.xy.y + inputDOF.xy.y
            self.robotDOF.xy.theta = self.robotDOF.xy.theta + inputDOF.xy.theta
            return True
        else:
            return False

    def checkMovement(self, lineMovement):
        for obs in self.obstacles:
            if obs.checkLineSegCross(lineMovement) is not None:
                return False
        else:
            return True

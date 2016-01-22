__author__ = 'xiongyi'
import ThreeDOF
from LineSegment import *
import SimulatorUtility


class Simulator:

    def __init__(self):
        self.pathTrackOn = True;
        self.height = 400
        self.width = 600
        self.time = 0.0
        self.TIMEINC = 0.1
        self.robotDOF = ThreeDOF.ThreeDOF()
        self.utility = SimulatorUtility.SimulatorUtility(self)
        self.obstacle = SimulatorUtility.SimulatorUtility.initObstacles(self)

    def nextStep(self):
        self.time += self.TIMEINC
        print(self.robotDOF.xy.x, self.robotDOF.xy.y, self.robotDOF.theta)
        SimulatorUtility.SimulatorUtility.drawSimulator(self);

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
        for obs in self.obstacle:
            if obs.checkLineSegCross(lineMovement) is not None:
                return False
        else:
            return True



if __name__ == '__main__':
    import threading
    sim = Simulator()
    sim.nextStep()
    t = threading.Timer(.5, sim.nextStep())
    t.start();

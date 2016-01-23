from LineSegment import LineSegment
import numpy as np
import math
__author__ = 'xiongyi'

bins_num = 9
degs = np.linspace(0, 2*math.pi, num=bins_num)
print('degrees  ', degs)

class SimulatorMeasure:
    def __init__(self):
        None

    @staticmethod
    def measure(sim):

        measureDists = []
        measureHits = []
        for deg in degs:
            line = SimulatorMeasure.makeObserveLineSeg(sim, deg, sim.robotDOF.xy.x, sim.robotDOF.xy.y)
            print('\ndeg = ', deg, line.sx, line.sy, line.ex, line.ey)

            if line is None:
                raise "measure LineSegment generate failed"
            try:
                [minDist, xyRet] = SimulatorMeasure.findClosestIntersect(sim, line, deg)
            except:
                print("error data: ")
                print("line = ", line.sx, line.sy, line.ex, line.ey)
                raise
            measureDists.append(minDist)
            measureHits.append(xyRet)
        sim.measureDists = measureDists
        sim.measureHits = measureHits


    @staticmethod
    def findClosestIntersect(sim, line, deg):
        minDist = math.inf
        xyRet = None
        limit = 10e-7
        for obs in sim.obstacles:
            xy = obs.checkLineSegCross(line)
            if xy is not None:
                l1 = xy[0]-line.sx
                l2 = xy[1]-line.sy
                dist = math.sqrt(l1*l1+l2*l2)
                sin_Sign = xy[1] - line.sy
                cos_Sign = xy[0] - line.sx
                if math.fabs(sin_Sign) > limit and math.fabs(cos_Sign) > limit:
                    if minDist > dist and math.sin(deg)*sin_Sign >= 0 and math.cos(deg)*cos_Sign >= 0:
                        minDist = dist
                        xyRet = xy
                elif math.fabs(sin_Sign) < limit and minDist > dist:
                    if math.cos(deg)*cos_Sign >= 0:
                        minDist = dist
                        xyRet = xy
                elif math.fabs(cos_Sign) < limit and minDist > dist:
                    if math.sin(deg)*sin_Sign >= 0:
                        minDist = dist
                        xyRet = xy

        if xyRet is None:
            raise "failed measure, hit no obstacles"
        print('xy = ', xyRet)
        return [minDist, xyRet]

    @staticmethod
    def makeObserveLineSeg(sim, deg, x0, y0):
        limit = 10e-6
        pi = math.pi
        if math.fabs(deg - pi/2) < limit:
            return LineSegment(x0, y0, x0, sim.y1+20)
        elif math.fabs(deg - pi) < limit:
            return LineSegment(x0, y0, sim.x0-10, y0)
        elif math.fabs(deg - pi/2*3) < limit:
            return LineSegment(x0, y0, x0, sim.y0-10)
        elif math.fabs(deg) < limit:
            return LineSegment(x0, y0, sim.x1+10, y0)
        l1 = (sim.width + sim.height) * 2
        x1 = x0 + math.cos(deg)*l1
        y1 = y0 + math.sin(deg)*l1
        # print('generate numerical line',   pi)
        return LineSegment(x0, y0, x1, y1)






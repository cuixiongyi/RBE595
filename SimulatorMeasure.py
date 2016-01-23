from Simulator import Simulator
from LineSegment import LineSegment
import numpy as np
import math
__author__ = 'xiongyi'

bins_num = 8
degs = np.arange(0, 2*math.pi, bins_num)
print(degs)

@staticmethod
def SimulatorMeasure(sim):
    measureDists = []
    measureHits = []
    for deg in degs:
        line = SimulatorMeasure.makeObserveLineSeg(deg, sim.robotDOF.xy.x, sim.robotDOF.xy.y)
        if line is None:
            raise "measure LineSegment generate failed"
        [minDist, xyRet] = findClosestIntersect(sim, line)
        measureDists.append(minDist)
        measureHits.append(xyRet)


@staticmethod
def findClosestIntersect(sim, line):
    minDist = math.inf
    xyRet = None
    for obs in sim.obstacles:
        xy = obs.checkLineSegCross(line)
        if xy is not None:
            dist = math.sqrt(xy[0]^2+xy[1]^2)
            if minDist > dist:
                minDist = dist
                xyRet = xy
    if xyRet is None:
        raise "failed measure, hit no obstacles"
    return [minDist, xyRet]

@staticmethod
def makeObserveLineSeg(sim, deg, x0, y0):
    limit = 10e-8
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
    return LineSegment(x0, y0, x1, y1)






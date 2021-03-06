from Simulator import Simulator
from Simulator.Geometry import LineSegment
import math
import numpy as np


class Astar:
    def __init__(self, sim, map):
        self.map = map
        self.obstacles = sim.obstacles


    # input start Coordinate, goal Coor
    def calculate(self, start, goal):
        self.goal = self.map.coor2Bin(goal.x, goal.y)
        self.start = self.map.coor2Bin(start.x, start.y)
        if self.goal is None:
            raise "A* algorithm: no goal is specified"
        open_set = set()
        closed_set = set()

        current = self.start
        open_set.add(current)

        while open_set:
            current = min(open_set, key=lambda bin: bin.G + bin.H)
            line_move = LineSegment.LineSegment(current.x0, current.y0, self.goal.x0, self.goal.y0)
            if Simulator.Simulator.checkMovement(self.obstacles, line_move):
                path = []
                path.append(self.goal)

                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]

            open_set.remove(current)
            closed_set.add(current)


            neighbor = []
            if current.id.binX > 0 :
                binTmp = self.map.bins[current.id.binX-1][current.id.binY]
                if self.testBin(current, binTmp):
                    neighbor.append(binTmp)
            if current.id.binX < self.map.map_width_bin_num-1:
                binTmp = self.map.bins[current.id.binX+1][current.id.binY]
                if self.testBin(current, binTmp):
                    neighbor.append(binTmp)
            if current.id.binY < self.map.map_height_bin_num-1:
                binTmp = self.map.bins[current.id.binX][current.id.binY+1]
                if self.testBin(current, binTmp):
                    neighbor.append(binTmp)
            if current.id.binY > 0:
                binTmp = self.map.bins[current.id.binX][current.id.binY-1]
                if self.testBin(current, binTmp):
                    neighbor.append(binTmp)

            g_inc = self.map.bin_size
            for bin in neighbor:
                if bin in closed_set:
                    continue

                if bin in open_set:
                    g = current.G + g_inc
                    if bin.G > g:
                        bin.G = g
                        bin.parent = current
                else:
                    bin.G = current.G + g_inc
                    bin.H = self.manhattan(bin)
                    bin.parent = current
                    open_set.add(bin)
        raise "no path found"





    def manhattan(self, bin):
        return math.fabs(bin.x0-self.goal.x0) + math.fabs(bin.y0-self.goal.y0)

    def testBin(self, current, binTmp):
        line_move = LineSegment.LineSegment(current.x0, current.y0, binTmp.x0, binTmp.y0)
        return Simulator.Simulator.checkMovement(self.obstacles, line_move)










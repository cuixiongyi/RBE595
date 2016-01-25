import Simulator.Simulator
import numpy as np


class Astar:
    def __init__(self, sim, map):
        self.map = map
        self.obstacles = sim.obstacles

    def calculate(self, start, end):
        self.goal = end
        if self.goal is None:
            raise "A* algorithm: no goal is specified"
        


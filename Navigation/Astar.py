import Simulator.Simulator
import numpy as np

map_bin_num = 200
map_height_bin_num = map_bin_num
map_width_bin_num = 0

class Astar:
    def __init__(self, sim):
        self.bin_size = sim.height / map_bin_num
        map_width_bin_num = map_bin_num * sim.width / sim.height
        self. grid = [[0]*map_height_bin_num] * map_width_bin_num

    def

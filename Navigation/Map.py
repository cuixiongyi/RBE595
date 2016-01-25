import Navigation.SimpleMapBin as Bin
import math
__author__ = 'xiongyi'


map_width_bin_num_g = 0
map_height_bin_num_g = 0

class Map:
    def __init__(self, sim):
        self.map_bin_num = 100
        self.map_height_bin_num = self.map_bin_num
        self.bin_size = sim.height / self.map_bin_num
        self.map_width_bin_num = round(self.map_bin_num * sim.width / sim.height)

        global map_height_bin_num_g
        map_height_bin_num_g = self.map_height_bin_num
        global map_width_bin_num_g
        map_width_bin_num_g = self.map_width_bin_num

        self.sim = sim

        self.bins = []
        half_bin_size = 0.5 * self.bin_size
        for ii in range(0, self.map_width_bin_num-1):
            self.bins.append([])
            for jj in range(0, self.map_height_bin_num-1):
                binTmp = Bin.SimpleMapBin(ii*self.bin_size+half_bin_size,
                                         jj*self.bin_size+half_bin_size,
                                         ii, jj)
                self.bins[-1].append(binTmp)

    # @staticmethod
    def coor2Bin(self, x0, y0):
        binX = round((x0 - self.sim.x0) / self.bin_size)
        binY = round((y0 - self.sim.y0) / self.bin_size)
        if binX in range(0, map_width_bin_num_g) and binY in range(0, map_height_bin_num_g):
            return self.bins[binX][binY]
        else:
            raise "cooridnate out of range"





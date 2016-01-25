import Navigation.SimpleMapBin as Bin
__author__ = 'xiongyi'


map_bin_num = 200
map_height_bin_num = map_bin_num
map_width_bin_num = 0


class Map:
    def __init__(self, sim):
        global map_width_bin_num
        global map_height_bin_num
        self.bin_size = sim.height / map_bin_num
        map_width_bin_num = map_bin_num * sim.width / sim.height
        self.bins = []
        half_bin_size = 0.5 * self.bin_size
        for ii in range(0, map_width_bin_num-1):
            self.bins.append([])
            for jj in range(0, map_height_bin_num-1):
                binTmp = Bin.SimpleMapBin(ii*self.bin_size+half_bin_size,
                                         jj*self.bin_size+half_bin_size,
                                         ii, jj)
                self.bins[-1].append(binTmp)







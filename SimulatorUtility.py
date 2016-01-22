import ThreeDOF
from LineSegment import *
import matplotlib.pyplot as plt
import matplotlib.lines as mline
import math
import numpy as np
__author__ = 'xiongyi'

obstaclesStyle = '-b'
robotDiamiter = 12;

circleStep = 50
robotBodyX = np.cos(np.linspace(0,2*math.pi, num=circleStep))*robotDiamiter
robotBodyY = np.sin(np.linspace(0,2*math.pi, num=circleStep))*robotDiamiter

class SimulatorUtility:
    def __init__(self, sim):
        self.fig = sim.fig
        rect = [0,0,sim.width, sim.height]
        self.ax = self.fig.add_axes(rect)
        self.lines, = self.ax.plot([],[], '-')
        # self.ax.set_xlim(sim.width, sim.height)
        # self.fig.show()


    def initObstacles(self, sim):

        obstacle = []
        obstacle.append(LineSegment(0,0,0,sim.height))
        obstacle.append(LineSegment(0,sim.height,sim.width,sim.height))
        obstacle.append(LineSegment(sim.width,sim.height,sim.width,0))
        obstacle.append(LineSegment(sim.width,0,0,0))

        obstacle.append(LineSegment(100, 100, 100, 50))
        obstacle.append(LineSegment(100, 50, 50, 50))
        obstacle.append(LineSegment(50, 50, 50, 100))
        obstacle.append(LineSegment(50, 100, 100, 100))

        obstacle.append(LineSegment(200, 300, 250, 400))
        obstacle.append(LineSegment(250, 400, 300, 100))
        obstacle.append(LineSegment(300, 100, 200, 300))

        return obstacle


    def drawLine(self, sim, style):
        xdata = [0]
        ydata = [0]
        for line in sim.obstacles:
            if line.sx == xdata[-1]:
                xdata.append(line.sx)
                xdata.append(line.ex)
                ydata.append(line.sy)
                ydata.append(line.ey)
            else:
                self.lines.set_xdata(xdata)
                self.lines.set_ydata(ydata)
                self.ax.plot(xdata,ydata, obstaclesStyle)
                # self.ax.add_line(self.lines)

                # self.lines = mline.Line2D(xdata,ydata)
                xdata = [line.sx, line.ex]
                ydata = [line.sy, line.ey]
        self.ax.plot(xdata,ydata, obstaclesStyle)

        # xdata.append(sim.obstacles[0].sx)
        # ydata.append(sim.obstacles[0].sy)

        # plt.plot([lineSeg.sx,lineSeg.ex], [lineSeg.sy, lineSeg.ey], style)

    def drawRobot(self, x, y, theta):
        y1 = robotDiamiter * math.sin(theta) + y
        x1 = robotDiamiter * math.cos(theta) + x
        # self.ax.Circle((x,y), radius=robotDiamiter, color='g', fill=False)
        self.ax.plot([x,x1],[y,y1], '-b', linewidth=2)
        self.ax.plot(robotBodyX+x,robotBodyY+y)
        # self.ax.p

    def drawSimulator(self, sim):
        self.fig.clf()
        self.ax = self.fig.gca(xlim=[0,sim.width], ylim=[0,sim.height])
        self.ax.hold(True)

        # rect = [0,0,, sim.height]

        self.drawLine(sim, obstaclesStyle)
        self.drawRobot(sim.robotDOF.xy.x, sim.robotDOF.xy.y, sim.robotDOF.theta)
        # self.ax.relim()
        # self.fig.show();

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()




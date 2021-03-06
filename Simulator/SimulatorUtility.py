from Simulator.Geometry.LineSegment import *

__author__ = 'xiongyi'

StyleObstacles = '-k'
StyleMeasure = '--b'
robotDiamiter = 12;

circleStep = 50
circlePointX = np.cos(np.linspace(0,2*math.pi, num=circleStep))
circlePointY = np.sin(np.linspace(0,2*math.pi, num=circleStep))

class SimulatorUtility:
    def __init__(self, sim):
        self.fig = sim.fig
        rect = [sim.x0,sim.y0,sim.x1, sim.y1]
        self.ax = self.fig.add_axes(rect)
        self.lines, = self.ax.plot([],[], '-')
        # self.ax.set_xlim(sim.width, sim.height)
        # self.fig.show()


    def initObstacles(self, sim):

        obstacle = []
        obstacle.append(LineSegment(sim.x0,sim.y0,sim.x0,sim.y1))
        obstacle.append(LineSegment(sim.x0,sim.y1,sim.x1,sim.y1))
        obstacle.append(LineSegment(sim.x1,sim.y1,sim.x1,sim.y0))
        obstacle.append(LineSegment(sim.x1,sim.y0,sim.x0,sim.y0))

        obstacle.append(LineSegment(100, 100, 100, 50))
        obstacle.append(LineSegment(100, 50, 500, 50))
        obstacle.append(LineSegment(500, 50, 500, 100))
        obstacle.append(LineSegment(500, 100, 100, 100))

        obstacle.append(LineSegment(200, 300, 250, 400))
        obstacle.append(LineSegment(300, 100, 200, 300))
        obstacle.append(LineSegment(250, 400, 300, 100))

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
                self.ax.plot(xdata,ydata, StyleObstacles)
                # self.ax.add_line(self.lines)

                # self.lines = mline.Line2D(xdata,ydata)
                xdata = [line.sx, line.ex]
                ydata = [line.sy, line.ey]
        self.ax.plot(xdata,ydata, StyleObstacles)

        # xdata.append(sim.obstacles[0].sx)
        # ydata.append(sim.obstacles[0].sy)

        # plt.plot([lineSeg.sx,lineSeg.ex], [lineSeg.sy, lineSeg.ey], style)

    def drawRobot(self, x, y, theta):
        y1 = robotDiamiter * math.sin(theta) + y
        x1 = robotDiamiter * math.cos(theta) + x
        # self.ax.Circle((x,y), radius=robotDiamiter, color='g', fill=False)
        self.ax.plot([x,x1],[y,y1], '-b', linewidth=2)
        self.ax.plot(circlePointX*robotDiamiter+x,circlePointY*robotDiamiter+y)
        # self.ax.p

    def drawMeasure(self, sim):
        if sim.measureHits is None:
            return
        x0 = sim.robotDOF.xy.x
        y0 = sim.robotDOF.xy.y
        for xy in sim.measureHits:
            self.ax.plot([x0,xy[0]],[y0,xy[1]], StyleMeasure)

    def drawGoalArea(self, sim):
        if sim.goal is None:
            return
        goalArea = 25
        self.ax.plot(circlePointX*goalArea+sim.goal.x,circlePointY*goalArea+sim.goal.y)


    def drawAStar(self, sim):
        if sim.astarPathX is None:
            return
        self.ax.plot(sim.astarPathX, sim.astarPathY)

    def drawSimulator(self, sim):
        self.fig.clf()
        self.ax = self.fig.gca(xlim=[sim.x0,sim.x1], ylim=[sim.y0,sim.y1])
        self.ax.hold(True)

        # rect = [0,0,, sim.height]

        self.drawLine(sim, StyleObstacles)
        self.drawRobot(sim.robotDOF.xy.x, sim.robotDOF.xy.y, sim.robotDOF.theta)
        self.drawMeasure(sim)
        self.drawGoalArea(sim)
        self.drawAStar(sim)
        # self.ax.relim()
        # self.fig.show();

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()




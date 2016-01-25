__author__ = 'xiongyi'
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Simulator.Simulator
from Periodic import Periodic

class Application(tk.Frame):
    def __init__(self, master=None):
        matplotlib.use('TkAgg')
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



    def createWidgets(self):

        self.fig = Figure(figsize=(5,4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0, columnspan=3)
        sim = Simulator.Simulator.Simulator(self.fig, self.canvas)
        # sim.run()
        self.timer = Periodic(0.3, sim.run)
        self.timer.start()


        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=1)

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.grid(row=2)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
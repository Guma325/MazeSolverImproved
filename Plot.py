import MazeSolver
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, MAZE_SOLVER):
        self.MAZE_SOLVER = MAZE_SOLVER

    def add_plot_line(self, LABEL):
        plt.plot(self.MAZE_SOLVER.EXIT_FILLED_LIST, label=LABEL)

    def show(self):
        plt.legend()
        plt.show()
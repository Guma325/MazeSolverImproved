# Maze Solver - Applying the dead end filling algorithm with heuristic improvement
# Algorithm made by Júlio César Guimarães Costa (05/09/2022)

import cv2
import random as rd
import glob
import os
import SolverAgent as sa
import numpy as np

class MazeSolver:

    def __init__(self, IMG_PATH, POSSIBLE_PATH, EXIT, WALL, DEAD_END_WALL, SAVE_VIDEO_IMGS=False):
        # EXECUTION CONSTANTS
        self.POSSIBLE_PATH = POSSIBLE_PATH  # The paths color
        self.WALL = WALL  # The wall color
        self.EXIT = EXIT  # The color that will mark the exits
        self.DEAD_END_WALL = DEAD_END_WALL  # The color that will mark the dead end
        self.IMG_PATH = IMG_PATH # Maze image path
        self.SAVE_VIDEO_IMGS = SAVE_VIDEO_IMGS
        self.MAZE_ITERATIONS = None
        self.EXIT_FILLED_LIST = None
        self.CURRENT_SOLUTION_MODE = None
        self.AGENT_LIST = None
        self.IMG = None
        self.setup()

    def setup(self):
        self.MAZE_ITERATIONS = 0
        self.EXIT_FILLED_LIST = []
        self.AGENT_LIST = []
        self.IMG = cv2.imread(self.IMG_PATH, 0)  # Read´s the maze file
        self.mark_exits()

    # find exits and mark them
    def mark_exits(self):
        for c, cell in enumerate(self.IMG[0]):
            if cell == self.POSSIBLE_PATH:
                self.IMG[0, c] = self.EXIT
        for c, cell in enumerate(self.IMG[-1]):
            if cell == self.POSSIBLE_PATH:
                self.IMG[-1, c] = self.EXIT
        for r, rows in enumerate(self.IMG):
            if rows[0] == self.POSSIBLE_PATH:
                self.IMG[r, 0] = self.EXIT
            if rows[-1] == self.POSSIBLE_PATH:
                self.IMG[r, -1] = self.EXIT

    # return boolean
    def is_dead_end(self, x, y):
        counter = 0
        left_cell = self.IMG[x - 1, y]
        right_cell = self.IMG[x + 1, y]
        up_cell = self.IMG[x, y + 1]
        down_cell = self.IMG[x, y - 1]
        if left_cell == self.WALL or left_cell == self.DEAD_END_WALL:
            counter += 1
        if right_cell == self.WALL or right_cell == self.DEAD_END_WALL:
            counter += 1
        if up_cell == self.WALL or up_cell == self.DEAD_END_WALL:
            counter += 1
        if down_cell == self.WALL or down_cell == self.DEAD_END_WALL:
            counter += 1
        if counter == 3:
            return True
        return False

    def populate_agent_list(self):
        ind = 0
        for x, rows in enumerate(self.IMG): # up-down iteration
            for y, cols in enumerate(rows): # right-left iteration
                if self.IMG[x, y] == self.POSSIBLE_PATH and self.is_dead_end(x, y):
                    self.AGENT_LIST.append(sa.SolverAgent(ind, x, y))
                    ind += 1

    # iteration starts at up-left
    def up_left_iteration(self):
        exit_count = 0
        self.MAZE_ITERATIONS += 1
        for x, rows in enumerate(self.IMG): # up-down iteration
            for y, cols in enumerate(rows): # right-left iteration
                if self.IMG[x, y] == self.POSSIBLE_PATH and self.is_dead_end(x, y):
                    self.IMG[x, y] = self.DEAD_END_WALL
                    exit_count += 1
                if self.SAVE_VIDEO_IMGS: cv2.imwrite("temp_imgs/" + str(self.MAZE_ITERATIONS) + ".png", self.IMG)
        self.EXIT_FILLED_LIST += [exit_count]
        return exit_count

    # iteration starts at up-right
    def up_right_iteration(self):
        exit_count = 0
        self.MAZE_ITERATIONS += 1
        for x, rows in enumerate(self.IMG): # up-down iteration
            for y, cols in reversed(list(enumerate(rows))): # left-right iteration
                if self.IMG[x, y] == self.POSSIBLE_PATH and self.is_dead_end(x, y):
                    self.IMG[x, y] = self.DEAD_END_WALL
                    exit_count += 1
                    if self.SAVE_VIDEO_IMGS: cv2.imwrite("temp_imgs/" + str(self.MAZE_ITERATIONS) + ".png", self.IMG)
        self.EXIT_FILLED_LIST += [exit_count]
        return exit_count

    # iteration starts at down-left
    def down_left_iteration(self):
        exit_count = 0
        self.MAZE_ITERATIONS += 1
        for x, rows in reversed(list(enumerate(self.IMG))): # down-up iteration
            for y, cols in enumerate(rows): # right-left iteration
                if self.IMG[x, y] == self.POSSIBLE_PATH and self.is_dead_end(x, y):
                    self.IMG[x, y] = self.DEAD_END_WALL
                    exit_count += 1
                    if self.SAVE_VIDEO_IMGS: cv2.imwrite("temp_imgs/" + str(self.MAZE_ITERATIONS) + ".png", self.IMG)
        self.EXIT_FILLED_LIST += [exit_count]
        return exit_count

    # iteration starts at down-right
    def down_right_iteration(self):
        exit_count = 0
        self.MAZE_ITERATIONS += 1
        for x, rows in reversed(list(enumerate(self.IMG))): # down-up iteration
            for y, cols in reversed(list(enumerate(rows))): # left-right iteration
                if self.IMG[x, y] == self.POSSIBLE_PATH and self.is_dead_end(x, y):
                    self.IMG[x, y] = self.DEAD_END_WALL
                    exit_count += 1
                    if self.SAVE_VIDEO_IMGS: cv2.imwrite("temp_imgs/" + str(self.MAZE_ITERATIONS) + ".png", self.IMG)
        self.EXIT_FILLED_LIST += [exit_count]
        return exit_count

    # Maze Solvers
    def solve(self, mode):
        self.setup()
        self.CURRENT_SOLUTION_MODE = mode

        if mode == "up_down":
            while True:
                if self.up_left_iteration() == 0: break

        if mode == "rotation":
            while True:
                if self.up_left_iteration() == 0:
                    break
                if self.down_right_iteration() == 0:
                    break
                if self.up_right_iteration() == 0:
                    break
                if self.down_left_iteration() == 0:
                    break

        if mode == "random_rotation":
            while True:
                randNum = rd.randint(0, 3)
                if randNum == 0:
                    if self.up_left_iteration() == 0:
                        break
                if randNum == 1:
                    if self.down_right_iteration() == 0:
                        break
                if randNum == 2:
                    if self.up_right_iteration() == 0:
                        break
                if randNum == 3:
                    if self.down_left_iteration() == 0:
                        break

        if mode == "agent":
            self.populate_agent_list()
            for agent in self.AGENT_LIST:
                while True:
                    newMaze = agent.move(self.IMG, self.POSSIBLE_PATH, self.DEAD_END_WALL, self.EXIT)
                    if isinstance(newMaze, np.ndarray):
                        self.IMG = newMaze
                        self.MAZE_ITERATIONS += 1
                    else:
                        break
                if self.SAVE_VIDEO_IMGS:
                    cv2.imwrite("temp_imgs/" + str(self.MAZE_ITERATIONS) + ".png", self.IMG)

    # Save Solution
    def save_solution(self, path=""):
        cv2.imwrite(path + self.IMG_PATH.split('.')[0] + "_" + str(self.MAZE_ITERATIONS) + "_solved.png", self.IMG)

    def save_solution_video(self, temp_imgs_path="", save_path="", fps=15):
        size = (len(self.IMG), len(self.IMG[0]))
        list_of_files = glob.glob(temp_imgs_path + "*")
        if len(list_of_files) == 0: raise ValueError("Set the SAVE_VIDEO_IMGS parameter to True when creating the maze solver object.")
        list_of_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        out = cv2.VideoWriter(save_path + self.IMG_PATH.split('.')[0] + "_" + str(self.MAZE_ITERATIONS) + "_" + self.CURRENT_SOLUTION_MODE + ".avi",
                              cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                              fps,
                              size)

        for filename in list_of_files:
            out.write(cv2.imread(filename))

        out.release()
        # clean imgs temp directory
        for filename in list_of_files:
            os.remove(filename)
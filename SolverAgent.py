class SolverAgent:
    def __init__(self, ind, xPos, yPos):
        self.ind = ind
        self.xPos = xPos
        self.yPos = yPos

    # return boolean
    def move(self, maze_map, possible_path, dead_end, exits):
        counter, nextX, nextY = 0, 0, 0
        left_cell = maze_map[self.xPos - 1, self.yPos]
        right_cell = maze_map[self.xPos + 1, self.yPos]
        up_cell = maze_map[self.xPos, self.yPos + 1]
        down_cell = maze_map[self.xPos, self.yPos - 1]
        if left_cell == possible_path or left_cell == exits:
            counter += 1
            nextX, nextY = self.xPos - 1, self.yPos
        if right_cell == possible_path or right_cell == exits:
            counter += 1
            nextX, nextY = self.xPos + 1, self.yPos
        if up_cell == possible_path or up_cell == exits:
            counter += 1
            nextX, nextY = self.xPos, self.yPos + 1
        if down_cell == possible_path or down_cell == exits:
            counter += 1
            nextX, nextY = self.xPos, self.yPos - 1
        if counter == 1:
            maze_map[self.xPos, self.yPos] = dead_end
            self.xPos, self.yPos = nextX, nextY
            return maze_map
        else:
            return False
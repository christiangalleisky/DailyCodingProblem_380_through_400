class ToePlitz():

    def __init__(self, N_by_N_matrix):
        self.grid = N_by_N_matrix

    def printTPMatrix(self):
        i = 0
        while i < len(self.grid):
            print(self.grid[i])
            i += 1

    def getDimensions(self):
        height = len(self.grid)
        width = len(self.grid[0])
        return height, width #heighth is the most external, #width is the most internal sub array

    def limits(self):
        height, width = self.getDimensions()
        y, x = 0, 0
        while True:
            bool = self.check_i_column_and_j_row(y, x) #column, row
            y += 1
            x += 1
            if (y == height and x == width) or bool == False:
                break
        return bool

    def check_i_column_and_j_row(self, i, j):
        z, iters = 0, len(self.grid)
        while z < iters:
            if self.grid[z][i] != self.grid[j][z]:
                return False
            z += 1
        return True


tpMatrix = [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]
obj = ToePlitz(tpMatrix)
obj.printTPMatrix()
print(obj.limits())
import pdb
class Solver():
    def __init__(self):
        self.m_ = 4
        self.n_ = 5
        self.stack_ = set()
        self.queue_ = set()

    def add_neighbours(self, x, y, grid):
        if x+1 < self.m_ and grid[x+1][y] == '1':
                self.stack_.add((x+1, y))
        if y+1 < self.n_ and grid[x][y+1] == '1':
                self.stack_.add((x, y+1))
        if x-1 >= 0 and grid[x-1][y] == '1':
                self.stack_.add((x-1, y))
        if y-1 >= 0 and grid[x][y-1] == '1':
                self.stack_.add((x, y-1))

    def bfs(self, grid):
        while len(self.stack_):
            x, y = self.stack_.pop()
            self.add_neighbours(x, y, grid)
            grid[x][y] = 'v'

    def dfs(self, grid):
        while len(self.queue_):
            x, y = self.queue_[0]
            del self.queue_[0]
            self.add_neighbours(x, y, grid)
            grid[x][y] = 'v'

    def solve(self, grid):
        self.m_, self.n_ = len(grid), len(grid[0])
        x, y = 0, 0
        r_value = 0

        while x < self.m_ and y < self.n_:
            if grid[x][y] == '1':
                self.add_neighbours(x, y, grid)

                grid[x][y] = 'v'
                r_value += 1

                if len(self.stack_):
                    self.bfs(grid)

            y += 1
            if y == self.n_:
                x += 1
                y = 0
        return r_value

def eq(exp, res):
    assert exp == res, res

def main():
    input = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    input2 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    input3 = [
        ['0', '0'],
        ['0', '0'],
    ]

    input4 = [
        ['1', '1'],
        ['1', '1'],
    ]

    s = Solver()
    eq(3, s.solve(input))
    eq(1, s.solve(input2))
    eq(0, s.solve(input3))
    eq(1, s.solve(input4))
    print('Success')

if "__main__" == __name__:
    main()
"""
  Instruction for the candidate.
    1) You are an avid rock collector who lives in southern California. Some rare
       and desirable rocks just became available in New ork, so you are planning
       a cross-country road trip. There are several other rare rocks that you could
       pick up along the way.

       You have been given a grid filled with numbers, representing the number of
       rare rocks available in varous cities across the country. Your objective
       is to find the optimal path from So_Cal to New York that would allow you to
       accumulate the most rocks along the way.

       Note: You can only travel either north (up) or east (right)
    2) Consider adding some additional tests in doTestPass()
    3) Implement optimalPath() correctly
    4) Here is an example:                         ^
                   [[0,0,0,0,5], New York (end)    N
                    [0,1,1,1,0],               < W   E >
    So_cal (start)  [2,0,0,0,0]]                   S
                                                   v
"""

def find_max(x, y, rows, cols, val, dp):
    west, south = 0, 0
    if x + 1 < rows:
        west = dp[x+1][y]
    if y - 1 >= 0:
        south = dp[x][y-1]
    return max(west, south) + val


def add_neighbours(x, y, rows, cols, queue):
    if x - 1 >= 0:
        queue.add((x-1, y))
    if y + 1 < cols:
        queue.add((x, y+1))


def optimal_path(grid):
    m_, n_ = len(grid), len(grid[0])
    queue = {(m_-1, 0)}

    # this should be redused to only previous state
    dp = [[0] * n_ for _ in range(m_)]

    while queue:
        x, y = queue.pop()
        add_neighbours(x, y, m_, n_, queue)
        dp[x][y] = find_max(x,y,m_,n_,grid[x][y], dp)

    return dp[0][n_-1]


def eq(exp, res):
    assert exp == res, f'expected: {exp} result: {res}'


def main():
    input = [
        [[0,0,0,0,5],
         [0,1,1,1,0],
         [2,0,0,0,0]],
        [[0,0,0,0,5],
         [0,1,1,1,0],
         [2,0,0,0,100]]
    ]

    expected = [10, 107]

    for i, o in zip(input, expected):
        eq(o, optimal_path(i))

    print('success')

if __name__ == '__main__':
    main()
def solve(grid, callback):
    """Finds a solution to a backtracking problem.

    grid     -- a 2d grid map of '1's (working space) and '0's (wall), count the number of offices. 
An office is surrounded by walls and is formed by connecting adjacent offices horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by walls.
    safe_up_to -- a function with two arguments, solution and position, that
                  returns whether the values assigned to slots 0..pos in
                  the solution list, satisfy the problem constraints.
    size       -- the total number of “slots” you are trying to fill

    Return the solution as a list of values.
    """
    solution = 0
    backtrack = False
    end = False

    def extend_solution(position, solution, end):
        solution = solution + 1
        while not end:
            if callback(grid, position, '0'):
                if position >= len(grid) or extend_solution(position+1, solution, end):
                    return solution
        return solution

    return extend_solution(0, solution,end)


def no_walls(grid, position, wall):
    # See if the sequence filled from indices 0 to up_to_index, inclusive, has
    # no walls of any adjancent substrings. We'll have to try all subsequences of
    # length 1, 2, 3, up to half the length of the string. Return False as soon
    # as we find a wall.
    for j in range(len(grid)):
        if (grid[j] == wall):
            print('Hit wall at: ', j)
            return False
    return True



        


if __name__ == "__main__":
    #grid = ['1','1','1','1','0']
    grid = [['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']]
    solution = [[0]*len(grid[0]) for _ in range(len(grid[0]))]
    def solve(r, c):
            if(r == len(grid) and c == len(grid[r])):
                solution[r][c] = 1
                return True
            
            if r>=0 and c>=0 and r < len(grid) and c < len(grid[r]) and grid[r][c] == '1':
                solution[r][c] = 1
                if solve(r, c+1):
                    return True
                if solve(r+1, c):
                    return True
                if solve(r, c-1):
                    return True
                if solve(r-1, c):
                    True
                solution[r][c] = 0
                #backtrack
                return False
            return 0
    print(solve(0,0))
    

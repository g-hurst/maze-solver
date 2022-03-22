import numpy as np
import re

def get_maze(path):
    maze = [x for x in open(path, 'r')][1:]
    for i, line in enumerate(maze):
        maze[i] = re.sub(r'(START-->\s|\s<--END)', '', line.strip())
        maze[i] = np.array(list(maze[i]))
    boolMaze = np.empty(np.shape(maze))
    boolMaze = (np.array(maze) == ' ')
    return boolMaze

def printPretty(mz):
    for row in mz:
        for point in row:
            if point: print(' ', end='')
            else:     print('#', end='')
        print('')
        
class Node:
    def __init__(self, value, child=None):
        self.child  = child
        self.value  = value
    def set_child(self, child):
        self.child = child
    def get_child(self):
        return self.child
    def get_value(self):
        return self.value

def find_start(mz):
    for i in range(len(mz)):
        if mz[i][0]:
            return (i, 0)        

def dfs(visited, graph, node):
    pass
    

if __name__ == '__main__':
    maze_paths = ['mazes\maze0.txt', 'mazes\maze1.txt', 'mazes\maze2.txt', 'mazes\maze3.txt', 'mazes\maze4.txt']
    # for path in maze_paths:
    #     maze = get_maze(path)
    #     printPretty(maze)
    #     print()
    maze = get_maze(maze_paths[0])

    printPretty(maze)
    
    visits = set()
    node_start = Node(find_start(maze))
    path = dfs(visits, maze, node_start)
    print('visits=', visits)
    print('path=', path)

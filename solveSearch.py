import numpy as np
import copy
import re
from enum import Enum

class SpaceType(Enum):
    WALL    = 0
    PATH    = 1
    VISITED = 2

def get_maze(path):
    in_maze = [x for x in open(path, 'r')][1:]
    for i, line in enumerate(in_maze):
        in_maze[i] = re.sub(r'(START-->\s|\s<--END)', '', line.strip())
        in_maze[i] = np.array(list(in_maze[i]))
    out_maze = np.empty(np.shape(in_maze), dtype=SpaceType)
    for i in range(len(out_maze)):
        for j in range(len(out_maze[i])):
            if in_maze[i][j] == '#':    out_maze[i][j] = SpaceType.WALL
            elif in_maze[i][j] == ' ':  out_maze[i][j] = SpaceType.PATH
            else:                       out_maze[i][j] = SpaceType.VISITED       
    return out_maze

def printPretty(mz):
    for row in mz:
        for point in row:
            if   point == SpaceType.PATH:    print(' ', end='')
            elif point == SpaceType.WALL:    print('#', end='')
            elif point == SpaceType.VISITED: print('o', end='')
        print('')
  
class Node:
    def __init__(self, value, child=None, parent=None):
        self.child   = child
        self.value   = value
        self.parent  = parent
    
    # setters
    def set_child(self, child):
        self.child = child
    def set_parent(self, parent):
        self.parent = parent
        
    # getters
    def get_parent(self):
        return self.parent
    def get_child(self):
        return self.child
    def get_value(self):
        return self.value
    

def find_neighbors(node, maze):
    points = [(node.value[0] + x, node.value[1] + y) for x, y in [(1,0), (0,1), (-1,0), (0,-1)]]
    xMax, yMax = np.shape(maze)
    for p in copy.copy(points):
        if   p[0] < 0 or p[0] > xMax - 1:                    points.remove(p)
        elif p[1] < 0 or p[1] > yMax - 1:                    points.remove(p)
        elif maze[p[0]][p[1]] == SpaceType.WALL:             points.remove(p)
        elif node.parent != None and p == node.parent.value: points.remove(p)
    return points

def find_start(mz):
    for i in range(len(mz)):
        if mz[i][0] == SpaceType.PATH:
            return (i, 0)        

def dfs(node, mz, visited=None):  
    if visited == None:
        visited = set()
    visited.add(node.value)
    for point in find_neighbors(node, mz):
        next_node = Node(point, parent=node)
        node.set_child(next_node)
        # if next_node.value[1] == len(mz[0]) - 1:
        #    return True
        dfs(next_node, mz, visited)
    return visited
    
if __name__ == '__main__':
    maze_paths = ['mazes\maze0.txt', 'mazes\maze1.txt', 'mazes\maze2.txt', 'mazes\maze3.txt', 'mazes\maze4.txt']
    # for path in maze_paths:
    #     maze = get_maze(path)
    #     printPretty(maze)
    #     print()
    maze = get_maze(maze_paths[0])

    printPretty(maze)
    
    first_node = Node(find_start(maze), maze)
    visits = dfs(first_node, maze)

    for p in visits:
        maze[p[0]][p[1]] = SpaceType.VISITED
    
    printPretty(maze)

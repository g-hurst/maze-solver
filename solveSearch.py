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
    print('')
  
class Node:
    def __init__(self, value, child=None, parent=None):
        self.child   = []
        self.child.append(child)
        self.value   = value
        self.parent  = parent
    
    # setters
    def add_child(self, child):
        self.child.append(child)
    def set_parent(self, parent):
        self.parent = parent
        
    # getters
    def get_parent(self):
        return self.parent
    def get_child(self):
        return self.child
    def get_value(self):
        return self.value
    
# finds the starting point of the maze
def find_start(mz):
    for i in range(len(mz)):
        if mz[i][0] == SpaceType.PATH:
            return (i, 0)        

def find_path(node, mz):
    # function that returns the open spaces next to the node
    def find_neighbors(node, maze):
        points = [(node.value[0] + x, node.value[1] + y) for x, y in [(1,0), (0,1), (-1,0), (0,-1)]]
        xMax, yMax = np.shape(maze)
        for p in copy.copy(points):
            if   p[0] < 0 or p[0] > xMax - 1:                    points.remove(p)
            elif p[1] < 0 or p[1] > yMax - 1:                    points.remove(p)
            elif maze[p[0]][p[1]] == SpaceType.WALL:             points.remove(p)
            elif node.parent != None and p == node.parent.value: points.remove(p)
        return set(points)
    
    # function that walks through the maze until a dead end is reached
    def walk(node, mz, visited=None):  
        if visited == None:
            visited = set()
        visited.add(node.value)
        points = find_neighbors(node, mz) - visited
        if len(points) != 0:
            point = points.pop()
            next_node = Node(point, parent=node)
            node.add_child(next_node)
            return walk(next_node, mz, visited)
        else:
            return node

    visited = set()
    best_path = set()

    # solves the maze and creates a tree of nodes with the root node as the entrance
    tracking_node = walk(node, mz, visited)
    while tracking_node.value[1] != len(mz[0]) - 1:
        #backtraces unitl the next path is found
        while len(find_neighbors(tracking_node, mz) - visited) == 0:
            tracking_node = tracking_node.parent        
        tracking_node = walk(tracking_node, mz, visited)
    
    # gets the optimal path
    while tracking_node.parent != None:
        best_path.add(tracking_node.value)
        tracking_node = tracking_node.parent

    return best_path
    
if __name__ == '__main__':
    maze_paths = ['mazes\maze0.txt', 'mazes\maze1.txt', 'mazes\maze2.txt', 'mazes\maze3.txt', 'mazes\maze4.txt']

    for path in maze_paths:
        maze = get_maze(path)

        print(path)
        printPretty(maze)

        root_node = Node(find_start(maze), maze)
        best_path = find_path(root_node, maze)

        for p in best_path:
            maze[p[0]][p[1]] = SpaceType.VISITED
        
        printPretty(maze)
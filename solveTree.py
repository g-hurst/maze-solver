import numpy as np
import copy
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

def printTree(tree):
    if len(tree.children) > 0:
        print('val= ', tree.value)
        for child in tree.children:
            printTree(child)
  
class Tree:
    def __init__(self, value, maze, parent=None):
        self.parent    = parent
        self.value     = value
        self.children = self.__find_children__(maze)
    def get_value(self):
        return self.value
    def __find_children__(self, maze):
        points = [(self.value[0] + x, self.value[1] + y) for x, y in [(1,0), (0,1), (-1,0), (0,-1)]]
        xMax, yMax = np.shape(maze)
        for p in copy.copy(points):
            if   p[0] < 0 or p[0] > xMax - 1:                    points.remove(p)
            elif p[1] < 0 or p[1] > yMax - 1:                    points.remove(p)
            elif not maze[p[0]][p[1]]:                           points.remove(p)
            elif self.parent != None and p == self.parent.value: points.remove(p)
        
        children = [Tree(p, maze, parent=self) for p in points]            
        
        return children

def find_start(mz):
    for i in range(len(mz)):
        if mz[i][0]:
            return (i, 0)        

def dfs(visited, node):
    pass
    if node not in visited:
        visited.add(node)
        for n in node.neighbors:
            dfs(visited, n)
    return 'you made it'
    

if __name__ == '__main__':
    maze_paths = ['mazes\maze0.txt', 'mazes\maze1.txt', 'mazes\maze2.txt', 'mazes\maze3.txt', 'mazes\maze4.txt']
    # for path in maze_paths:
    #     maze = get_maze(path)
    #     printPretty(maze)
    #     print()
    maze = get_maze(maze_paths[0])

    printPretty(maze)
    
    visits = set()
    tree = Tree(find_start(maze), maze)
    
    print('visits=', visits)

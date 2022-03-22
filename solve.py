import numpy as np
import re

maze = np.array([re.sub(r'(START-->\s| <--END)', '', x.strip()) for x in open('mazes/maze0.txt', 'r')][1:])

def printPretty(mz):
    for l in mz:
        print(l, end = '\t')
        print(len(l) == 25, end = '\t')
        print(np.where(mz == l))
        
printPretty(maze)
# maze-solver

### About
This project was created to model the way a person would solve a maze. No, the algorithm is not the MOST efficient due to this fact. The inspiration for this came from an ENGR 16200 group project where we were tasked with building small, autonomous maze solving robots. Ultimately, this project helped me gain some background knowledge on maze traversal and path finding before the final project implementation. Convieniently, this project was written shortly after my [maze generator project](https://github.com/g-hurst/maze-generator), so the mazes to be solved in this project were generated from there. 

### Some Other Info
* only solves text based mazes of '#'s and spaces (' ')
* the algorithm is meant to "walk" through the maze like a physical thing would

### ALgorithm
This algorithm is a modified version of a depth first search. Instead of backtracking recersivly to traverse a new path, the backtracking is hard coded into the algorithm. This was done in order to model how a physical object would traverse a maze.
1. walk unitl a dead end is reached
2. if the dead end is the exit, stop
3. else backtrack to the first branch that has not yet been traversed
4. return to `step 1`
# Maze Solver

This Python program is a simple maze-solving algorithm designed to guide a character (or robot) to the goal in a maze. It uses basic movement and decision-making logic to navigate the maze.

## Description

The program follows these steps:
1. Moves forward while the path ahead is clear.
2. Turns left when the forward path is blocked and starts exploring the maze.
3. At each step:
   - If the right side is clear, it turns right and moves forward.
   - If the front is clear, it moves forward.
   - If both are blocked, it turns left to find a new direction.

The logic ensures that the character eventually finds the goal.

## Functions

- `turn_right()`: A helper function that turns the character 90° to the right by making three left turns.
- `while front_is_clear()`: Moves forward until encountering an obstacle.
- `while not at_goal()`: Executes the maze-solving logic until the goal is reached.
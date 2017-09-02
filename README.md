# 2x2_Depth
Python script to solve the depth of a 2x2 Rubik's Cube.

# Running this code on your machine:
1. Have a functioning Python 2.7+ version installed
2. Clone this repository
3. Open a terminal and cd into src
4. Run python and import search
5. Run search.solve()

# Explanation of the Code

How a Position is Represented:
+ A position is represented by a string of sticker colors (W = White, G = Green, O = Orange, B = Blue, R = Red, Y = Yellow).
+ Each index represents the color that exists at a specific sticker position around the cube.
+ Position_Structure.png shows this exact path. Imagine the net as a cube (the indices just travel clockwise around the cube).
+ The moves assume an orientation of green front and white top.
+ The blue/orange/yellow corner is unlabeled because it serves as a reference corner and never moves (more details in moves.py explanation).

How moves.py Works:
+ This file hard codes all 9 moves that can be performed on a 2x2.
+ Left, Down, and Back moves are not needed.
  + For example, performing an R creates the exact same position as performing an L (at a different orientation).
  + The same applies for all of the moves on those three faces (they each have a partner on the opposite side).
  + As a result, the back/left/down corner never moves and serves as a reference.
  + This also verifies that no two positions are rotations of each other.
+ The stickers are returned in the order that they would exist upon performing that move to the cube.

How search.py Works:
+ The main loops generates a data structure that contains every position, categorized by depth.
+ Depth 0 is just the solved position and depth 1 is that position with every move applied to it.
+ From there, every move is applied to every position in the deepest set.
+ The uncategorized cases are assumed to be one level deeper.
+ This continues until no deeper cases are produced.

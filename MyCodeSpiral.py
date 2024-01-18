# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]
# w

# Example:

import math
X, Y, Z = Position()
radius = 10
y = -1
r = 0
for i in range(300):
  x = int(radius * math.cos(r))
  z = int(radius * math.sin(r))
  SetBlock((x, y, z), blocks[i % 4])
  y += 1
  r += 0.2

#
# DESCRIPTION:
#   Create a 10 x 10 pyramid
#
# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]
# w
s = 1  # step size

# Get our current position
X, Y, Z = Position()

# Move 20 blocks away
Z -= 20

# Remember that the y coordinate is up and down; not z
size = 10
n = size
for y in range(size):
  for x in range(-n, n):
    for z in range(-n, n):
      SetBlock((X+x, Y+y, Z+z), blocks[y % 4])
  n -= 1

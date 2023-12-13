# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]
# w
s = 1  # step size


X, Y, Z = Position()
for y in range(5):
  SetBlock((X+2, Y+y-1, Z), GRASS)
  SetBlock((X, Y+y-1, Z+2), SAND)
  SetBlock((X-2, Y+y-1, Z), BRICK)
  SetBlock((X, Y+y-1, Z-2), STONE)

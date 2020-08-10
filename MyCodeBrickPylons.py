#
# Draw some BRICK pillars in a square around you.
#
# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]

s = 2  # step size
X, Y, Z = Position()


w = 5

for y in range(Y-1,Y+w):
    z = -w
    for x in range(X-w, X+w+1, s):
         SetBlock((x, y, z), BRICK)
    x = -w
    for z in range(Z-w, Z+w+1, s):
         SetBlock((x, y, z), BRICK)
    z = w
    for x in range(X-w, X+w+1, s):
         SetBlock((x, y, z), BRICK)
    x = w
    for z in range(Z-w, Z+w+1, s):
         SetBlock((x, y, z), BRICK)

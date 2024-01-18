# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]
# w

# Example:


def f(t):
  return -20*t*t + 3*x

X, Y, Z = (0,0,10)

t = 0.0
dt = 0.05
for x in range(1000):
  y = f(t)
  print(x,y)
  SetBlock((X+t, Y+y, Z), SAND)
  t += dt
  if x < 0: break

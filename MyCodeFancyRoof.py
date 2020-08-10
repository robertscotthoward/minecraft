# GLOBALS:
blocks = [GRASS, SAND, BRICK, STONE]
s = 1  # step size
import math

X, Y, Z = Position()
Y -= 1

def Staircase():
  for i in range(100):
    for j in range(-5,6):
      SetBlock((X+j+5, Y+i, Z+i), blocks[j%4])

def Spiral():
  r = 10
  for ii in range(1000):
    i = ii/15
    for j in range(-1,3):
      SetBlock((X+(r+0.9*j)*math.cos(i), Y+4*i, Z+(r+0.9*j)*math.sin(i)), blocks[j%4])

# for y in range(10):
  # for i in range(-5,6):
    # SetBlock((X+i, Y+y, Z+5), blocks[i%4])
    # SetBlock((X+i, Y+y, Z-5), blocks[i%4])
    # SetBlock((X+5, Y+y, Z+i), blocks[i%4])
    # SetBlock((X-5, Y+y, Z+i), blocks[i%4])

for x in range(-100,101):
  for z in range(-100,101):
    SetBlock((X+x, Y+30, Z+z), blocks[(math.floor(math.sqrt(x*x+z*z)))%4])

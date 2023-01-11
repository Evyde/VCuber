import math
import time
from tkinter import Tk
from BasicDraw import BasicDraw
import Coordinates

MAX_X, MAX_Y = 640, 480

window = Tk()
window.title("VCuber - Made By Evyde")

a = BasicDraw(window, MAX_X, MAX_Y)

CUBE_LENGTH = 200

simple_cube = Coordinates.get_vertices(0, 0, 0, CUBE_LENGTH // 2)

print(simple_cube)

r = 0
j = 0


def test():
    global r, j
    if j % 2 == 0:
        r += math.pi / 1800
        a.clear()
        a.draw_cube(simple_cube, rot_z=r, rot_x=r, rot_y=r, trans_x=r, trans_y=r, trans_z=r, method="正")
    j += 1
    window.after(1, test)


test()
window.mainloop()

import tkinter as tk
import math
import random

RADIUS = 10
SEEDS = 10


def random_point(x, y):
    a = random_angle = 2*math.pi*random.random()
    r = random_radius = RADIUS*math.sqrt(random.random())
    random_x = r*math.cos(a)+x
    random_y = r*math.sin(a)+y
    return random_x, random_y


def paint(event):
    x = event.x
    y = event.y
    canvas = event.widget
    for i in range(SEEDS):
        random_x, random_y = random_point(x, y)
        canvas.create_line(random_x, random_y, random_x +
                           1, random_y+1, fill='black')


root = tk.Tk()
cnvs = tk.Canvas(root)
cnvs.bind('<Motion>', paint)
cnvs.pack()
root.mainloop()

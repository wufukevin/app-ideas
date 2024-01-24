import argparse
import random
import tkinter as tk
from tkinter import messagebox, ttk, Canvas, colorchooser
from PIL import Image, ImageTk
import subprocess
from ui import BaseApp
import os
from enum import Enum

# 1. api


class DrawingApp(BaseApp):
    def __init__(self, header_frame, content_frame, footer_frame, return_callback):
        self.selected_color = "red"
        self.width_of_line = 1
        self.mouse_x = 0
        self.mouse_y = 0
        super().__init__(header_frame, content_frame, footer_frame, return_callback)

    def create_widgets(self):
        canvas_width = 600
        canvas_height = 300
        self.cvs = Canvas(self.content_frame,
                    width=canvas_width,
                    height=canvas_height,
                    bg="white")
        self.cvs.pack()
        self.cvs.bind('<Button-1>', self.xy)
        self.cvs.bind('<B1-Motion>', self.addLine)

        cvs2 = Canvas(self.content_frame, width=canvas_width, height=40, bg="orange")
        cvs2.pack()

        bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
                   "hourglass","info", "questhead", "question", "warning"]
        nsteps = len(bitmaps)
        step_x = int(canvas_width / nsteps)

        for i in range(nsteps):
            cvs2.create_bitmap((i+1)*step_x - step_x/2, 20, bitmap=bitmaps[i])
        
        # line size scale
        self.size_scale = tk.Scale(self.content_frame, label="Width of line", from_=1,
                                   to=5, orient=tk.HORIZONTAL, command=self.update_width_of_line)
        self.size_scale.pack(pady=10)

        # Color frame to display selected color
        self.color_frame = tk.Frame(
            self.content_frame, width=30, height=30, bg=self.selected_color, borderwidth=1, relief="solid")
        self.color_frame.pack(padx=10)

        # Color button
        # can't change color of button ??
        self.color_button = tk.Button(
            self.content_frame, text="Select Color", command=self.choose_color, bg="yellow", background="blue")
        self.color_button.pack(pady=10)

        # Bind mouse events to the canvas
        # self.cvs.bind("<B1-Motion>", self.draw_rectangle)
        super().create_widgets()

    def xy(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def addLine(self, event):
        self.cvs.create_line((self.mouse_x, self.mouse_y, event.x, event.y),
                             fill=self.selected_color, width=self.width_of_line.get())
        self.mouse_x = event.x
        self.mouse_y = event.y
    
    def update_width_of_line(self, size):
        self.width_of_line = int(size)

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.selected_color)
        if color[1]:
            self.selected_color = color[1]
            self.color_button.configure(bg=self.selected_color)
            self.color_frame.configure(bg=self.selected_color)

    def draw_rectangle(self, event):
        x, y = event.x, event.y
        x1, y1 = x - self.width_of_line, y - self.width_of_line
        x2, y2 = x + self.width_of_line, y + self.width_of_line
        self.cvs.create_rectangle(
            x1, y1, x2, y2, fill=self.selected_color, outline="black")


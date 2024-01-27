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
        self.brush = ("none", "line", "rectangle", "circle")
        self.current_brush = self.brush[0]
        self.start_x = 0
        self.start_y = 0
        self.temp_img = None
        super().__init__(header_frame, content_frame, footer_frame, return_callback)

    def create_widgets(self):
        canvas_width = 600
        canvas_height = 300
        self.cvs = Canvas(self.content_frame,
                    width=canvas_width,
                    height=canvas_height,
                    bg="white")
        self.cvs.pack()
        self.cvs.bind('<Button-1>', self.start_draw)
        self.cvs.bind('<B1-Motion>', self.drawing)
        self.cvs.bind('<ButtonRelease-1>', self.stop_draw)

        self.cvs2 = Canvas(self.content_frame, width=canvas_width, height=40, bg="orange")
        self.cvs2.pack()
        self.cvs2.bind('<Button-1>', self.cvs2_click)

        # bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
        #            "hourglass","info", "questhead", "question", "warning"]
        # nsteps = len(bitmaps)
        # step_x = int(canvas_width / nsteps)

        # for i in range(nsteps):
        #     self.cvs2.create_bitmap((i+1)*step_x - step_x/2, 20, bitmap=bitmaps[i], tags = bitmaps[i])
        
        for i in range(len(self.brush)):
            self.cvs2.create_text(60*(i+1), 20, text=self.brush[i], tags = self.brush[i], fill="blue")
        
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
        
        # Clear button
        self.clear_button = tk.Button(
            self.header_frame, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.RIGHT, padx=10)

        # Generate pdf button
        self.generate_pdf_button = tk.Button(
            self.header_frame, text="Generate PDF", command=self.generate_pdf)
        self.generate_pdf_button.pack(side=tk.RIGHT, padx=10)

        super().create_widgets()

    def cvs2_click(self, event):
        currently_clicked = self.cvs2.find_withtag("current")
        if currently_clicked:
            self.current_brush = self.cvs2.gettags("current")[0]
            
    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def stop_draw(self, event):
        self.end_x = event.x
        self.end_y = event.y
        if self.current_brush == self.brush[0]:
            pass
        elif self.current_brush == self.brush[1]:
            pass
        elif self.current_brush == self.brush[2]:
            self.finished_rectangle = self.cvs.create_rectangle(
                self.start_x, self.start_y, self.end_x, self.end_y, fill=self.selected_color, outline="black", width=self.width_of_line)
            self.cvs.delete(self.temp_img)
            self.temp_img = None
        elif self.current_brush == self.brush[3]:
            self.finished_circle = self.cvs.create_oval(
                self.start_x, self.start_y, self.end_x, self.end_y, fill=self.selected_color, outline="black", width=self.width_of_line)
            self.cvs.delete(self.temp_img)
            self.temp_img = None

    def drawing(self, event):
        if self.current_brush == self.brush[0]:
            pass
        elif self.current_brush == self.brush[1]:
            self.draw_line(event)
        elif self.current_brush == self.brush[2]:
            self.draw_rectangle(event)
        elif self.current_brush == self.brush[3]:
            self.draw_circle(event)


    def draw_line(self, event):
        self.cvs.create_line((self.start_x, self.start_y, event.x, event.y),
                             fill=self.selected_color, width=self.width_of_line)
        self.start_x = event.x
        self.start_y = event.y
    
    def on_image_click(self, event):
        print(f"on_image_click {event}")

    def update_width_of_line(self, size):
        self.width_of_line = int(size)

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.selected_color)
        if color[1]:
            self.selected_color = color[1]
            self.color_button.configure(bg=self.selected_color)
            self.color_frame.configure(bg=self.selected_color)

    def draw_rectangle(self, event):
        self.cvs.delete(self.temp_img)
        self.temp_img = self.cvs.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, fill=self.selected_color, outline="black", width=self.width_of_line)
    
    def draw_circle(self, event):
        self.cvs.delete(self.temp_img)
        self.temp_img = self.cvs.create_oval(
            self.start_x, self.start_y, event.x, event.y, fill=self.selected_color, outline="black", width=self.width_of_line)
    def clear(self):
        self.cvs.delete("all")
    
    def generate_pdf(self):
        # Unable to locate Ghostscript on paths
        self.cvs.postscript(file="tmp.ps", colormode="color")
        image = Image.open("tmp.ps")
        image.save("output.jpg", 'jpeg')
        image.close()
        



import tkinter as tk
from tkinter import ttk, scrolledtext
import requests
from typing import Type
from ui import BaseApp

class Input_Class():
    def __init__(self, type: Type, name: str) -> None:
        self.type = type
        self.name = name
        pass

class MainApp:
    def __init__(self, root, app_list:list[Input_Class]):
        self.root = root
        self.root.title("Combined App")
        self.app_list = app_list

        self.create_homepage()

    def create_homepage(self):
        homepage_frame = tk.Frame(self.root)
        homepage_frame.pack(pady=20)

        ttk.Label(homepage_frame, text="Choose an App to Open:").grid(
            row=0, column=0, columnspan=2, pady=10)

        for i in range(len(self.app_list)):
            self.app_class = self.app_list[i]
            ttk.Button(homepage_frame, text=self.app_class.name,
                       command=self.create_app).grid(row=int(i/2)+1, column=int(i % 2), padx=10)

    def create_app(self):
        self.clear_frame()
        app_frame = tk.Frame(self.root)
        app_frame.pack(side=tk.BOTTOM, padx=10)
        self.app_class.type(app_frame, self.return_to_homepage)

    def return_to_homepage(self):
        self.clear_frame()
        self.create_homepage()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

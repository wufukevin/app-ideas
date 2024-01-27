import tkinter as tk
from tkinter import ttk, scrolledtext
import requests
from typing import Type
from game_ui import GameUI


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BattleShip Game")
        self.root.geometry("300x300")

        self.create_homepage()

    def create_homepage(self):
        homepage_frame = tk.Frame(self.root)
        homepage_frame.pack(pady=20)

        ttk.Button(homepage_frame, text="Start Game", command= self.start_game).grid(
            row=0, column=0, columnspan=2, pady=10)

    def start_game(self):
        self.clear_frame()
        header_frame = tk.Frame(self.root)
        content_frame = tk.Frame(self.root)
        footer_frame = tk.Frame(self.root)
        header_frame.pack(side=tk.TOP, padx=10)
        content_frame.pack(side=tk.TOP, padx=10)
        footer_frame.pack(side=tk.BOTTOM, padx=10)
        self.game_ui = GameUI(header_frame, content_frame,
                              footer_frame, self.return_to_homepage)

    def return_to_homepage(self):
        self.clear_frame()
        self.create_homepage()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

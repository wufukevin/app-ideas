import argparse
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from ui import BaseApp
import os
from enum import Enum

class CardState(Enum):
    HIDDEN = 0
    REVEALED = 1
    FINED = 2

class CardMemoryGameApp(BaseApp):
    def __init__(self, parent_frame, return_callback):
        self.rows = 3
        self.columns = 4
        self.clickable = True

        # List to store pairs of card images
        self.card_images = ['apple', 'banana', 'cherry', 'grape', 'orange',
                            'peach', 'apple', 'banana', 'cherry', 'grape', 'orange', 'peach']
        random.shuffle(self.card_images)

        # Dictionary to track the state of each card
        self.card_state = {}
        super().__init__(parent_frame, return_callback)

    def set_button_img(self, button: tk.Button, image_name):
        img = Image.open(
            os.getcwd()+f"/Projects/images/{image_name}.png")      # 開啟圖片
        resized_img = img.resize((50, 50))
        tk_img = ImageTk.PhotoImage(resized_img)

        button.config(image=tk_img)
        button.image = tk_img  # Keep a reference to the image

    def create_widgets(self):
        self.buttons = []

        for row in range(self.rows):
            for col in range(self.columns):
                index = row * self.columns + col

                button = tk.Button(
                    self.parent_frame, command=lambda r=row, c=col: self.card_click(r, c))
                self.set_button_img(button, "white")
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)
                self.card_state[(row, col)] = {
                    'image': self.card_images[index], 'state': CardState.HIDDEN}
        self.return_button = tk.Button(
            self.parent_frame, text="Reset", command=self.reset_game)
        self.return_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        super().create_widgets()

    def card_click(self, row, col):
        # Ignore clicks on already revealed cards
        if self.card_state[(row, col)]['state'] != CardState.HIDDEN or not self.clickable:
            return

        # Reveal the clicked card
        index = row * self.columns + col
        self.set_button_img(self.buttons[index], self.card_images[index])
        self.card_state[(row, col)]['state'] = CardState.REVEALED

        # Check for a match
        revealed_cards = [(r, c) for (
            r, c), data in self.card_state.items() if data['state'] == CardState.REVEALED]
        if len(revealed_cards) == 2:
            self.clickable = False
            if self.card_state[revealed_cards[0]]['image'] == self.card_state[revealed_cards[1]]['image']:
                self.parent_frame.after(10, lambda: self.hide_cards(
                    revealed_cards, finished=True))
            else:
                self.parent_frame.after(1000, lambda: self.hide_cards(revealed_cards))

    def hide_cards(self, cards, finished=False):
        if(finished): messagebox.showinfo("Match", "You found a match!")
        for (row, col) in cards:
            self.set_button_img(
                self.buttons[row * self.columns + col], "black" if finished else "white")
            self.card_state[(row, col)
                            ]['state'] = CardState.FINED if finished else CardState.HIDDEN
        self.clickable = True
    
    def reset_game(self):
        random.shuffle(self.card_images)
        for row in range(self.rows):
            for col in range(self.columns):
                index = row * self.columns + col
                self.set_button_img(self.buttons[index], "white")
                self.card_state[(row, col)] = {
                    'image': self.card_images[index], 'state': CardState.HIDDEN}
        self.clickable = True
        return None

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os


class CardMemoryGame(tk.Tk):
    def __init__(self, rows, columns):
        super().__init__()

        self.title("Card Memory Game")
        self.rows = rows
        self.columns = columns
        self.clickable = True

        # List to store pairs of card images
        self.card_images = ['apple', 'banana', 'cherry', 'grape', 'orange',
                            'peach', 'apple', 'banana', 'cherry', 'grape', 'orange', 'peach']
        random.shuffle(self.card_images)

        # Dictionary to track the state of each card
        self.card_state = {}

        self.create_widgets()
    
    def set_button_img(self, button:tk.Button, image_name):
        img = Image.open(
                    os.getcwd()+f"/Projects/images/{image_name}.png")      # 開啟圖片
        resized_img = img.resize((50, 50))
        tk_img = ImageTk.PhotoImage(resized_img) 

        button.config(image = tk_img)
        button.image = tk_img  # Keep a reference to the image
        print("kevin set button img finish")

    def create_widgets(self):
        self.buttons = []

        for row in range(self.rows):
            for col in range(self.columns):
                index = row * self.columns + col

                button = tk.Button(
                    self, command=lambda r=row, c=col: self.card_click(r, c))
                self.set_button_img(button, "white")
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)
                self.card_state[(row, col)] = {
                    'image': self.card_images[index], 'state': 'hidden'}
                
    def card_click(self, row, col):
        # Ignore clicks on already revealed cards
        if self.card_state[(row, col)]['state'] == 'revealed' or not self.clickable:
            return
        
        # Reveal the clicked card
        index = row * self.columns + col
        self.set_button_img(self.buttons[index], self.card_images[index])
        self.card_state[(row, col)]['state'] = 'revealed'

        # Check for a match
        revealed_cards = [(r, c) for (
            r, c), data in self.card_state.items() if data['state'] == 'revealed']
        if len(revealed_cards) == 2:
            self.clickable = False
            if self.card_state[revealed_cards[0]]['image'] == self.card_state[revealed_cards[1]]['image']:
                messagebox.showinfo("Match", "You found a match!")
                self.after(1000, lambda: self.hide_cards(revealed_cards, finished=True))
            else:
                self.after(1000, lambda: self.hide_cards(revealed_cards))

    def hide_cards(self, cards, finished=False):
        for (row, col) in cards:
            self.set_button_img(self.buttons[row * self.columns + col], "black" if finished else "white")
            self.card_state[(row, col)]['state'] = 'fined' if finished else 'hidden'
        self.clickable = True



if __name__ == "__main__":
    game = CardMemoryGame(rows=3, columns=4)
    game.mainloop()

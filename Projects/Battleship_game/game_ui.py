import tkinter as tk
from game_engine import Battleship_engine


class GameUI:
    def __init__(self, header_frame, content_frame, footer_frame, return_callback, width=9, height=9):
        self.header_frame = header_frame
        self.content_frame = content_frame
        self.footer_frame = footer_frame
        self.return_callback = return_callback
        self.width = width
        self.height = height
        self.engine = Battleship_engine(self.width-1, self.height-1)
        self.shoot_x = tk.StringVar()
        self.shoot_y = tk.StringVar()
        self.create_widgets()
    
    def draw_chessboard(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0:
                    tk.Label(self.content_frame, text=f"{j}", width=2, height=1).grid(
                        row=i, column=j)
                else:
                    tk.Label(self.content_frame, text=f"{i}" if j == 0 else "", width=2, height=1).grid(
                        row=i, column=j)

    def create_widgets(self):
        # Draw the header
        tk.Button(self.header_frame, text="Radar", command=self.show_ships).pack(
            side=tk.RIGHT, padx=10, pady=10)

        self.draw_chessboard()

        # Draw shoot button
        tk.Label(self.footer_frame, text="X:").pack(
            side=tk.LEFT, padx=10, pady=10)
        self.x_entry = tk.Entry(self.footer_frame, textvariable=self.shoot_x, validate="key", validatecommand=(
            self.footer_frame.register(self.validate_amount), '%P'), width=2)
        self.x_entry.pack(side=tk.LEFT, padx=10, pady=10)
        tk.Label(self.footer_frame, text="Y:").pack(
            side=tk.LEFT, padx=10, pady=10)
        self.y_entry = tk.Entry(self.footer_frame, textvariable=self.shoot_y, validate="key", validatecommand=(
            self.footer_frame.register(self.validate_amount), '%P'), width=2)
        self.y_entry.pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.footer_frame, text="Shoot", command=self.shoot).pack(
            side=tk.LEFT, padx=10, pady=10)
        
        # Reset Button
        self.reset_button = tk.Button(
            self.footer_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.BOTTOM, pady=10)

        # Return to Homepage Button
        self.return_button = tk.Button(
            self.footer_frame, text="Return", command=self.return_callback)
        self.return_button.pack(side=tk.BOTTOM, pady=10)
        return None
    
    def validate_amount(self, value):
        if value == '':
            return True
        elif str.isdigit(value):
            num = int(value)
            if 0 < num < self.width:
                return True
        return False

        
    def shoot(self):
        x = int(self.shoot_x.get())
        y = int(self.shoot_y.get())
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        if self.engine.shoot(x, y):
            tk.Label(self.content_frame, text="X", width=2, height=1).grid(
                row=y, column=x)
        else:
            tk.Label(self.content_frame, text="O", width=2, height=1).grid(
                row=y, column=x)
        if self.engine.is_game_over():
            self.reset_button.config(text="Game Over")
            self.shoot_x.set("")
            self.shoot_y.set("")

    def show_ships(self):
        for ship in self.engine.placed_ships:
            for point in ship:
                tk.Label(self.content_frame, text="X", width=2, height=1).grid(
                    row=point.y+1, column=point.x+1)
        self.reset_button.config(text="Game Over")
                
    def reset(self):
        self.engine = Battleship_engine(self.width-1, self.height-1)
        self.reset_button.config(text="Reset")
        self.draw_chessboard()
        self.shoot_x.set("")
        self.shoot_y.set("")
        return None

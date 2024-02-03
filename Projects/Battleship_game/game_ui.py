import tkinter as tk
from game_engine import Battleship_engine


class GameUI:
    def __init__(self, header_frame, content_frame, footer_frame, return_callback, width=9, height=9, player_count=2):
        self.header_frame = header_frame
        self.content_frame = content_frame
        self.footer_frame = footer_frame
        self.return_callback = return_callback
        self.width = width
        self.height = height
        self.player_count = player_count
        self.current_player = 0
        self.engine = Battleship_engine(
            self.width-1, self.height-1, player_count=self.player_count)
        self.shoot_x = tk.StringVar()
        self.shoot_y = tk.StringVar()
        self.create_widgets()
    
    def draw_chessboard(self):
        for player_number in range(self.player_count):
            for y in range(self.height):
                self.update_chessboard(player_number+1, -3, y, " ")
                self.update_chessboard(player_number+1, -2, y, "|")
                self.update_chessboard(player_number+1, -1, y, " ")
                for x in range(self.width):
                    if y == 0:
                        self.update_chessboard(player_number, x, y, f"{x}")
                    else:
                        self.update_chessboard(
                            player_number, x, y, f"{y}" if x == 0 else "")
                    

    def update_chessboard(self, player_number, x, y, text):
        tk.Label(self.content_frame, text=text, width=2, height=1).grid(
            row=y, column=x+player_number*(self.width+3))

    def create_widgets(self):
        # Draw the header
        tk.Button(self.header_frame, text="Radar", command=self.show_ships).pack(
            side=tk.RIGHT, padx=10, pady=10)

        # Draw the content of chessboard
        self.draw_chessboard()

        # Draw info of current player
        self.player_label = tk.Label(self.footer_frame, text=f"Player {self.current_player+1}")
        self.player_label.pack(side=tk.TOP, padx=10, pady=10)

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
        
        # Draw reset Button
        self.reset_button = tk.Button(
            self.footer_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.BOTTOM, pady=10)

        # Draw return to Homepage Button
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

        
    def update_player(self):
        self.current_player = (self.current_player + 1) % self.player_count
        self.player_label.config(text=f"Player {self.current_player+1}")

    def shoot(self):
        x = int(self.shoot_x.get())
        y = int(self.shoot_y.get())
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.update_chessboard(self.current_player, x, y, "X" if self.engine.shoot(x-1, y-1) else "O")
        self.update_player()
        if self.engine.is_game_over():
            self.reset_button.config(text="Game Over")
            self.shoot_x.set("")
            self.shoot_y.set("")

    def show_ships(self):
        for battlefield_data in self.engine.battlefield_data:
            for ship in battlefield_data.placed_ships:
                for point in ship.ship_location:
                    self.update_chessboard(battlefield_data.player_number, point[0]+1, point[1]+1, "X")
        self.reset_button.config(text="Game Over")
                
    def reset(self):
        self.engine = Battleship_engine(
            self.width-1, self.height-1, player_count=self.player_count)
        self.reset_button.config(text="Reset")
        self.draw_chessboard()
        self.shoot_x.set("")
        self.shoot_y.set("")
        self.current_player = 0
        return None

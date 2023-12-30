import tkinter as tk
from tkinter import ttk
from ui import BaseUI

class mainAPP(BaseUI):
    def __init__(self, root):
        super().__init__(root)
        self.cities = {
            "Moscow": 3,
            "Paris": 2,
            "Berlin": 2,
            "Brussels": 2,
            "Amsterdam": 2,
            "Rome": 2,
            "London": 1,
            "Dublin": 1,
            "New York": -4,
            "Washington": -4,
            "St. Louis": -5,
            "Los Angeles": -7,
            "Tokyo": 9,
            "Beijing": 8,
            "Ho Chi Mihn City": 7,
            "Mumbai": 5,
        }
    
    def create_widgets(self):
        print("kevin child widget")
        # Timezone Finder Widgets
        self.gmt_label = tk.Label(self.parent_frame, text="Enter GMT Offset:")
        self.gmt_label.pack(pady=5)
        self.gmt_entry = tk.Entry(self.parent_frame)
        self.gmt_entry.pack(pady=5)
        self.find_button = tk.Button(
            self.parent_frame, text="Find Cities", command=self.find_cities)
        self.find_button.pack(pady=10)

        self.timezone_output_text = tk.Text(
            self.parent_frame, height=10, width=30, wrap=tk.WORD)
        self.timezone_output_text.pack(pady=10)

        return super().create_widgets()

    def find_cities(self):
        gmt_offset = self.get_gmt_offset()
        cities_in_gmt = [city for city,
                         offset in self.cities.items() if offset == gmt_offset]
        self.display_results(cities_in_gmt, self.timezone_output_text)

    def get_gmt_offset(self):
        try:
            return int(self.gmt_entry.get())
        except ValueError:
            return 0

    def display_results(self, items, output_text_widget):
        output_text_widget.delete(1.0, tk.END)  # Clear previous results
        if items:
            for item in items:
                output_text_widget.insert(tk.END, f"{item}\n")
        else:
            output_text_widget.insert(tk.END, "No results found.")
        output_text_widget.yview(tk.END)

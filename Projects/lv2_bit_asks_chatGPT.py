import tkinter as tk
from tkinter import ttk, scrolledtext
import requests


class BookSearchApp:
    def __init__(self, parent_frame, return_callback):
        self.parent_frame = parent_frame
        self.return_callback = return_callback
        self.create_widgets()

    def create_widgets(self):
        # Book Search Widgets
        self.query_label = tk.Label(self.parent_frame, text="Book Search:")
        self.query_label.pack(pady=5)
        self.query_entry = tk.Entry(self.parent_frame)
        self.query_entry.pack(pady=5)
        self.search_button = tk.Button(
            self.parent_frame, text="Search Books", command=self.search_books)
        self.search_button.pack(pady=10)

        self.book_output_text = scrolledtext.ScrolledText(
            self.parent_frame, wrap=tk.WORD, width=40, height=10)
        self.book_output_text.pack(pady=10)

        # Return to Homepage Button
        self.return_button = tk.Button(
            self.parent_frame, text="Return to Homepage", command=self.return_callback)
        self.return_button.pack(pady=10)

    def search_books(self):
        query = self.query_entry.get()
        if query:
            self.show_loading()
            books = self.search_books_api(query)
            self.display_results(books, self.book_output_text)
            self.hide_loading()

    def search_books_api(self, query):
        GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": query}
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            return []

    def show_loading(self):
        self.book_output_text.insert(tk.END, "Loading...\n")
        self.book_output_text.yview(tk.END)

    def hide_loading(self):
        pass  # You can customize this if needed

    def display_results(self, items, output_text_widget):
        output_text_widget.delete(1.0, tk.END)  # Clear previous results
        if items:
            for item in items:
                output_text_widget.insert(tk.END, f"{item}\n")
        else:
            output_text_widget.insert(tk.END, "No results found.")
        output_text_widget.yview(tk.END)


class TimezoneApp:
    def __init__(self, parent_frame, return_callback):
        self.parent_frame = parent_frame
        self.return_callback = return_callback
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
        self.create_widgets()

    def create_widgets(self):
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

        # Return to Homepage Button
        self.return_button = tk.Button(
            self.parent_frame, text="Return to Homepage", command=self.return_callback)
        self.return_button.pack(pady=10)

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


class CalculatorApp:
    def __init__(self, parent_frame, return_callback):
        self.parent_frame = parent_frame
        self.return_callback = return_callback
        self.create_widgets()

    def create_widgets(self):
        # Calculator Widgets
        self.expression_label = tk.Label(
            self.parent_frame, text="Enter Expression:")
        self.expression_label.pack(pady=5)
        self.expression_entry = tk.Entry(self.parent_frame)
        self.expression_entry.pack(pady=5)
        self.calculate_button = tk.Button(
            self.parent_frame, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.result_text = scrolledtext.ScrolledText(
            self.parent_frame, wrap=tk.WORD, width=40, height=10)
        self.result_text.pack(pady=10)

        # Return to Homepage Button
        self.return_button = tk.Button(
            self.parent_frame, text="Return to Homepage", command=self.return_callback)
        self.return_button.pack(pady=10)

    def calculate(self):
        expression = self.expression_entry.get()
        if expression:
            result = self.evaluate_expression(expression)
            self.display_result(result)

    def evaluate_expression(self, expression):
        try:
            # Additional Calculator Features
            if "+-" in expression:
                expression = expression.replace("+-", "-")
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def display_result(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Result: {result}")
        self.result_text.yview(tk.END)

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Combined App")

        self.create_homepage()

    def create_homepage(self):
        homepage_frame = tk.Frame(self.root)
        homepage_frame.pack(pady=20)

        ttk.Label(homepage_frame, text="Choose an App to Open:").grid(
            row=0, column=0, columnspan=2, pady=10)

        ttk.Button(homepage_frame, text="Book Search App",
                   command=self.open_book_search_app).grid(row=1, column=0, padx=10)
        ttk.Button(homepage_frame, text="Timezone App",
                   command=self.open_timezone_app).grid(row=1, column=1, padx=10)
        ttk.Button(homepage_frame, text="Calculator App"
                   , command=self.open_calculator_app).grid(row=1, column=2, padx=10)

    def open_calculator_app(self):
        self.clear_frame()
        calculator_frame = tk.Frame(self.root)
        calculator_frame.pack(side=tk.BOTTOM, pady=10)
        self.calculator_app = CalculatorApp(
            calculator_frame, self.return_to_homepage)

    def open_book_search_app(self):
        self.clear_frame()
        book_search_frame = tk.Frame(self.root)
        book_search_frame.pack(side=tk.LEFT, padx=10)
        self.book_search_app = BookSearchApp(
            book_search_frame, self.return_to_homepage)

    def open_timezone_app(self):
        self.clear_frame()
        timezone_frame = tk.Frame(self.root)
        timezone_frame.pack(side=tk.RIGHT, padx=10)
        self.timezone_app = TimezoneApp(
            timezone_frame, self.return_to_homepage)

    def return_to_homepage(self):
        self.clear_frame()
        self.create_homepage()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

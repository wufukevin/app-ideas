import tkinter as tk
from tkinter import scrolledtext
import requests
from ui import BaseApp


class BookSearchApp(BaseApp):
    def __init__(self, parent_frame, return_callback):
        super().__init__(parent_frame, return_callback)

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
        super().create_widgets()

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

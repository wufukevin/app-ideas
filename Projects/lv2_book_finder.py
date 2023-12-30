import tkinter as tk
from tkinter import scrolledtext
import requests


class BookSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Search App")

        self.create_widgets()

    def create_widgets(self):
        # Search Entry and Button
        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.pack(pady=5)
        self.query_entry = tk.Entry(self.root)
        self.query_entry.pack(pady=5)
        self.search_button = tk.Button(
            self.root, text="Search", command=self.search_books)
        self.search_button.pack(pady=5)

        # Loading Label
        self.loading_label = tk.Label(
            self.root, text="Loading...", fg="blue", font=("Helvetica", 12), pady=10)
        self.loading_label.pack_forget()

        # Results Text Area
        self.results_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=40, height=10)
        self.results_text.pack(pady=10)

    def search_books(self):
        query = self.query_entry.get()
        if query:
            self.show_loading()
            books = self.search_books_api(query)
            self.display_results(books)
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
        self.loading_label.pack()

    def hide_loading(self):
        self.loading_label.pack_forget()

    def display_results(self, books):
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        if books:
            for book in books:
                title = book.get("volumeInfo", {}).get("title", "N/A")
                authors = ", ".join(
                    book.get("volumeInfo", {}).get("authors", []))
                published_date = book.get("volumeInfo", {}).get(
                    "publishedDate", "N/A")
                description = book.get("volumeInfo", {}).get(
                    "description", "N/A")

                result_text = f"Title: {title}\nAuthors: {authors}\nPublished Date: {published_date}\nDescription: {description}\n\n"
                self.results_text.insert(tk.END, result_text)
        else:
            self.results_text.insert(tk.END, "No results found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookSearchApp(root)
    root.mainloop()

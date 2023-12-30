from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"


def search_books(query):
    params = {"q": query}
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        return []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        books = search_books(query)
        return render_template("index.html", books=books, query=query)
    return render_template("index.html", books=[], query="")


if __name__ == "__main__":
    app.run(debug=True)

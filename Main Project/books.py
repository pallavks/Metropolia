import requests
def fetch_book_details(title):

    query = "+".join(title.split())
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:

            book_data = data["items"][0]["volumeInfo"]
            author = ", ".join(book_data.get("authors", ["Unknown Author"]))
            summary = book_data.get("description", "No summary available.")
            return {
                "author": author,
                "summary": summary
            }
        else:
            print("No book found with that title.")
    else:
        print("Failed to connect to Google Books API.")

    return {
        "author": "Unknown Author",
        "summary": "No summary available."
    }

class Book:
    def __init__(self, title, author="Unknown", summary="No summary available."):
        self.title = title
        self.author = author
        self.summary = summary

    def __str__(self):
        return f"{self.title} by {self.author} | {self.summary}"

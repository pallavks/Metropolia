# library.py

import csv
from collections import defaultdict
from book import Book, fetch_book_details

MAX_BORROWED_BOOKS = 3
BOOKS_CSV_FILE = "books.csv"

class Library:
    def __init__(self):
        self.books = {}  # title -> Book instance
        self.borrowed_books = {}  # title -> member
        self.borrow_count = defaultdict(int)
        self.load_books_from_csv()

    def load_books_from_csv(self):
        try:
            with open(BOOKS_CSV_FILE, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    book = Book(row['title'], row['author'], row['summary'])
                    self.books[book.title] = book
        except FileNotFoundError:
            print(f"No CSV file found. Starting with an empty library.")

    def save_books_to_csv(self):
        with open(BOOKS_CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'author', 'summary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books.values():
                writer.writerow({
                    'title': book.title,
                    'author': book.author,
                    'summary': book.summary
                })

    def add_book(self, title):
        if title in self.books:
            print(f"'{title}' already exists.")
        else:
            details = fetch_book_details(title)
            book = Book(title, details["author"], details["summary"])
            self.books[title] = book
            self.save_books_to_csv()
            print(f"Added: {book}")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            self.save_books_to_csv()
            print(f"Removed '{title}' from library.")
        else:
            print(f"'{title}' not found in library.")

    def view_available_books(self):
        print("\nAvailable books:")
        for title, book in self.books.items():
            if title not in self.borrowed_books:
                print(f"- {book}")
        print()

    def borrow_book(self, member, title):
        if title not in self.books:
            print(f"Book '{title}' does not exist.")
        elif title in self.borrowed_books:
            print(f"Book '{title}' is already borrowed.")
        else:
            borrowed = [b for b, m in self.borrowed_books.items() if m == member]
            if len(borrowed) >= MAX_BORROWED_BOOKS:
                print(f"You cannot borrow more than {MAX_BORROWED_BOOKS} books.")
            else:
                self.borrowed_books[title] = member
                self.borrow_count[title] += 1
                print(f"{member} borrowed '{title}'.")

    def return_book(self, member, title):
        if self.borrowed_books.get(title) == member:
            del self.borrowed_books[title]
            print(f"{member} returned '{title}'.")
        else:
            print(f"You did not borrow '{title}'.")

    def view_borrowed_books(self):
        print("\nBorrowed books:")
        for title, member in self.borrowed_books.items():
            print(f"- {title} is borrowed by {member}")
        print()

    def view_most_popular_books(self):
        print("\nMost popular books:")
        for title, count in sorted(self.borrow_count.items(), key=lambda item: item[1], reverse=True):
            print(f"- {title}: borrowed {count} times")
        print()

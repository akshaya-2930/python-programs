class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = 'Available' if self.available else 'Borrowed'
        return f'"{self.title}" by {self.author} ({status})'


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}  # {user: [book1, book2]}

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f" - {book}")

    def display_borrowed(self):
        print("\nBorrowed Books:")
        for user, books in self.borrowed_books.items():
            print(f"{user} has borrowed:")
            for book in books:
                print(f"  - {book}")

    def borrow_book(self, title, user):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                self.borrowed_books.setdefault(user, []).append(book)
                print(f"\n{user} successfully borrowed {book.title}")
                return
        print("\nBook not available or doesn't exist.")

    def return_book(self, title, user):
        if user in self.borrowed_books:
            for book in self.borrowed_books

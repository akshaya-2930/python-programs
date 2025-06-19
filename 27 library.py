# Book data structure: book_id -> {"title": ..., "author": ..., "available": True/False}
library = {}

def add_book(book_id, title, author):
    if book_id in library:
        print("Book ID already exists.")
    else:
        library[book_id] = {"title": title, "author": author, "available": True}
        print(f"Book '{title}' added.")

def view_books():
    if not library:
        print("Library is empty.")
    else:
        for book_id, info in library.items():
            status = "Available" if info["available"] else "Checked out"
            print(f"{book_id}: {info['title']} by {info['author']} - {status}")

def borrow_book(book_id):
    book = library.get(book_id)
    if not book:
        print("Book not found.")
    elif not book["available"]:
        print(f"'{book['title']}' is currently borrowed.")
    else:
        book["available"] = False
        print(f"You borrowed '{book['title']}'.")

def return_book(book_id):
    book = library.get(book_id)
    if not book:
        print("Book not found.")
    elif book["available"]:
        print(f"'{book['title']}' was not borrowed.")
    else:
        book["available"] = True
        print(f"You returned '{book['title']}'.")

# Example usage
if __name__ == "__main__":
    add_book("B101", "1984", "George Orwell")
    add_book("B102", "The Alchemist", "Paulo Coelho")
    view_books()
    borrow_book("B101")
    view_books()
    return_book("B101")
    view_books()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"Failure, the book {self.title} is unavailable")
        else:
            self.is_borrowed = True
            print(f"Success, the book {self.title} is now borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Success, the book {self.title} is now returned")
        else:
            print(f"Failure, the book {self.title} was already returned")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book.title, book.is_borrowed)


library = Library()

library.add_book("Harry", "JK")
library.add_book("Harry2", "JK2")
library.add_book("Harry3", "JK3")

library.display_books()

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


newbook = Book("Harry Potter", "JK")
newbook.borrow()
newbook.return_book()
newbook.return_book()


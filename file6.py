class Library:
    
    # Constructor to initialize book details
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    # Method to check out a book
    def checkout(self):
        if self.available:
            self.available = False
            print(f'"{self.book_name}" has been checked out.')
        else:
            print(f'"{self.book_name}" is currently not available.')

    # Method to return a book
    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.book_name}" has been returned.')
        else:
            print(f'"{self.book_name}" was not issued.')

    # Method to display available books
    def display(self):
        if self.available:
            print(f'"{self.book_name}" by {self.author} is available.')
        else:
            print(f'"{self.book_name}" by {self.author} is not available.')


# Creating objects (books)
book1 = Library("Python Basics", "John Doe")
book2 = Library("Data Structures", "Jane Smith", False)

# Display status
book1.display()
book2.display()

# Perform operations
book1.checkout()
book1.checkout()   # trying again

book1.return_book()
book2.return_book()

# Final status
book1.display()
book2.display()
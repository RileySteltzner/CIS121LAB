class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author
    def set_author(self, value):
        self.author = value
    
    def display_info(self):
        print (f'{self.name} by {self.author}')
    
    def __str__(self):
        return f'{self.name} was written by {self.author}'

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def display_catalog(self):
        print(f"Library: {self.library_name}")
        print(f"Catalog:")
        for book in self.books:
            print(f" {book.title} by {book.author}")
    def __str__(self):
        return f'In the library there are 2 books{len(self.books)} books'
    

library1 = Library("BoomLib")
book1 = Book("Harry Potter", "JK Rowling")
book2 = Book("Maze Runner", "IDK")
library1.add_book(book1)
library1.add_book(book2)
library1.display_catalog()
print(library1)

    
    

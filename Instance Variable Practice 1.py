class Book:
    def __init__(self, title, author, ISBN, availabilty):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availabilty = availabilty
        
    def get_ISBN(self):
        return self.ISBN
    
class Library(object):
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author, ISBN, availabilty='available'):
        book = Book(title, author, ISBN, availabilty)
        self.books.append(book)
        
    def remove_book(self, ISBN):
        for book in self.books:
            if book.get_ISBN() == ISBN:
                self.books.remove(book)
    
    def borrow_book(self, ISBN):
        for book in self.books:
            if book.get_ISBN() == ISBN:
                book.availabilty = 'not available'
                
    def return_book(self, ISBN):
        for book in self.books:
            if book.get_ISBN() == ISBN:
                book.availabilty = 'available'
                
    def list_books(self):
        return [book.title for book in self.books]
    
        
library = Library()
library.add_book('Harry Potter', 'James Auston', 1)
library.add_book('The Last Day On Earth', 'James Gun', 2)


library.borrow_book(1)
print([book.availabilty for book in library.books])

print()
library.return_book(1)
print([book.availabilty for book in library.books])

print()
print(library.list_books())

print()
library.remove_book(1)
print(library.list_books())


class Library:
    def __init__(self):
        self.books_list = []
        
    def add_books(self, title, author, ISBN, available_copies):
        book = {title.lower():{'author':author, 'ISBN':ISBN, 'available_copies':available_copies}}
        self.books_list.append(book)
        return f'Book {title.title()} is added'
    
    def checkout_book(self, title):
        title = title.lower()
        for books in self.books_list:
            for key in books:
                if key == title:
                    if books[title]['available_copies'] > 0:
                        books[title]['available_copies'] = books[title]['available_copies'] - 1
                        return f'Book {title.title()} successfully checkout.'
        return f"Book {title.title()} is not available"
    
    def return_book(self, title):
        title = title.lower()
        for books in self.books_list:
            for key in books:
                if key == title:
                    books[title]['available_copies'] = books[title]['available_copies'] + 1
                    return f'Book {title} successfully returned.'
        
    def list_available_books(self):
        available_books = []
        for books in self.books_list:
            for key in books:
                available_books.append(key.title())
        return available_books
    
    def check_availability(self, title):
        title = title.lower()
        for books in self.books_list:
            for key in books:
                if key == title:
                    if books[title]['available_copies'] > 0:
                        return f"Book {title.title()} avaiable with {books[title]['available_copies']} copies."
                    elif books[title]['available_copies'] <= 0:
                        return f"Book {title.title()} copies is not avaiable."
        return f"Book {title.title()} is not available"
        
    
if __name__ == "__main__":   
    library1 = Library()
    print(library1.add_books('Harry Potter','James Auston', 3052515, 100))
    print(library1.add_books('Advanced Python','James Gun', 3052526, 500))
    print(library1.add_books('Harry Potter In Hogwards','James Auston', 3052166, 0))
    print(library1.checkout_book('Harry Potter'))
    
    print()
    print(library1.list_available_books())
    
    print()
    print(library1.check_availability('Harry Potter'))
    print(library1.return_book('Harry Potter'))
    print(library1.check_availability('Harry Potter'))
    
    print()
    print(library1.check_availability('Harry Potter'))
    
    print()
    print(library1.check_availability('harry Potter In Hogwards'))
    print(library1.checkout_book('harry Potter In Hogwards'))
    
    print()
    print(library1.return_book('harry Potter In Hogwards'))
    print(library1.check_availability('harry Potter In Hogwards'))


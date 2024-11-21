class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class Library:
    def __init__(self, name):
        self.name = name # this sets the name of the library
        self.book_list = [] # this creates an empty books_list for that library

    def add_book(self, book):
        self.book_list.append(book)
        
    def remove_book(self, book):
        for lib_book in self.book_list:
            if lib_book.title == book.title and lib_book.author == book.author:
                self.book_list.remove(lib_book)
            break
        
    def search_books(self, search_string):
        results = []
        search_string = search_string.lower()
        for book in self.book_list:
            if search_string in book.title.lower() or search_string in book.author.lower():
                results.append(book)
        return results
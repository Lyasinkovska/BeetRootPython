"""
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
 for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books

"""
from datetime import datetime


class Author:
    def __init__(self, name: str, country: str, birthday: str, books: list):

        self.name = name
        self.country = country
        try:
            self.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        except Exception:
            print('Wrong birthday format.')
            self.birthday = datetime.strptime('0001-01-01', '%Y-%m-%d').date()
        self.books = books

    def __str__(self):
        return f'author_name: {self.name}'

    def __repr__(self):
        return self.__str__()


class Book:
    books_amount = 0

    def __init__(self, name: str, year: int, author: Author):
        self.year = year
        self.name = name
        self.author = author
        Book.books_amount += 1

    def __str__(self):
        return f'\nbook_name: {self.name}, year: {self.year}, {self.author}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, new_book: Book):
        """
        returns an instance of Book class and adds the book to the books list for the current library.
        """
        if new_book.name in new_book.author.books:
            self.books.append(new_book)
        else:
            raise IndexError("The book is not found in authors list of books.")
        return new_book

    def group_by_author(self, author: Author):
        """
        returns a list of all books grouped by the specified author
        """
        return list(filter(lambda book: book.author == author, self.books))
        # return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        """
        returns a list of all the books grouped by the specified year
        """
        return list(filter(lambda book: book.year == year, self.books))
        # return [book for book in self.books if book.year == year]

    def __str__(self):
        return f'{self.name}:\n{self.books}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    author1 = Author("Stephen King", 'USA', '1947-9-21', ['The Shining', 'Under the Dome', 'Pet Sematary',
                                                            'Castle Rock'])
    author2 = Author('Fredrik Backman', 'Sweden', '1981-6-2', ['A Man Called Ove', 'Britt-Marie Was Here',
                                                                 'My Grandmother Asked Me to Tell You She\'s Sorry',
                                                                 'Us Against You'])
    library = Library('Central Library')
    book1 = Book('Castle Rock', 2018, author1)
    book2 = Book('A Man Called Ove', 2013, author2)
    book3 = Book('Britt-Marie Was Here', 2016, author2)
    book4 = Book('Us Against You', 2018, author2)
    library.new_book(book1)
    library.new_book(book2)
    library.new_book(book3)
    library.new_book(book4)
    print(library.group_by_author(author2))
    print(library.group_by_year(2010))
    print(library)
    print(author2.birthday)
    print(author1.birthday)
    author3 = Author("Name", "USA", '-', [])
    print(author3.birthday)
    print(Book.books_amount)



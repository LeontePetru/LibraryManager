class Book:

    def __init__(self, title, author, isbn, genre, publisher):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publisher = publisher

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

b1 = Book("a", "b", "c", "d", "e")

b1.title="abcsdcds"
b1.isbn="twee"

print(b1.isbn)


from Books import Book
from JSONPersistence import BookPersistence

class BooksInventory:

    def __init__(self):
        self.__bookPersistence=BookPersistence("library.json")
        self.__bookList = self.__bookPersistence.read()

    @property
    def bookPersistence(self):
        return self.__bookPersistence

    @bookPersistence.setter
    def bookPersistence(self, bookPersistence):
        self.__bookPersistence = bookPersistence

    @property
    def bookList(self):
        return self.__bookList

    @bookList.setter
    def bookList(self, bookList):
        self.__bookList = bookList


    def updateList(self,list):
        self.bookList=list

    def sort(self):
        pass

    def raport(self):
        pass



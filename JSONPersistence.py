import json
from Books import Book

class JSONPersist:

    def __init__(self, file):
        self.__file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file= file

    def serializeList(self,list):
        s = ""
        for i in list:
            s=s+json.dumps(i.__dict__,indent=2)+'\n'

        with open(self.file, 'w') as f:
            f.write(s)
        return

    def deserialize(self):
        with open(self.file, 'r') as file:
            data = file.read()
        return data;


class BookPersistence(JSONPersist):

    def __init__(self,file):
        super().__init__(file)

    def read(self):
        data=self.deserialize()
        splitted = data.split('}')
        n=splitted.__len__()

        bookList= []

        for i in range(n-1):
            auxData=json.loads(splitted[i]+"}")
            auxBook= Book(auxData['_Book__title'],auxData['_Book__author'],auxData['_Book__isbn'],
                          auxData['_Book__genre'],auxData['_Book__publisher'],auxData['_Book__inventoryNumber'],
                          auxData['_Book__state'])
            bookList.append(auxBook);

        return bookList

    def saveBook(self,book):
        bookList=self.read()
        bookList.append(book)
        self.serializeList(bookList)
        return True

    def deleteBook(self,inventoryNumber):
        bookList=self.read()
        newBookList=[]
        n=bookList.__len__()
        for i in range(n):
            if bookList[i].inventoryNumber!=inventoryNumber:
                newBookList.append(bookList[i])
        self.serializeList(newBookList)
        return True

    def searchByName(self,name):
        bookList=self.read()
        n = bookList.__len__()
        for i in range(n):
            if(bookList[i].title==name):
                return bookList[i]
        return False



            #print("object: {}".format(i))
            #print(splitted[i])
            #print("\n")


#b1 = Book("Amintiri din copilarie", "Ion Creanga", "928-008-123", "Memorii", "P45","12","have")

#b2 = Book("Amintiri din copilarie2", "Ion Creanga2", "928-008-123", "Memorii2", "P452","333","borrowed")

#b3 = Book("Amintiri din copilarie24", "Ion Creanga24", "928-008-1234", "Memorii24", "P4524","3334","borrowed4")

#library = []
#library.append(b1);
#library.append(b2);



#pers = BookPersistence("library.json")

#print(pers.searchByName("Amintiri din copilarie").__dict__)
#pers.deleteBook(333)
#
#pers.serializeList(library)
#bookL=pers.read()

#pers.saveBook(b2)
#pers.saveBook(b3)

#pers.deleteBook("333")







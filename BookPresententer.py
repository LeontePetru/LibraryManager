
from BooksInventory import BooksInventory


class BookPresenter:

    def __init__(self):
        self.__bookInventory=BooksInventory()

    @property
    def bookInventory(self):
        return self.__bookInventory

    @bookInventory.setter
    def bookInventory(self, bookInventory):
        self.__bookInventory = bookInventory

    def stringOfBooks(self):
        listOfString= []
        books=self.bookInventory.bookList
        n=books.__len__()

        for i in range(n):
            stringGen=[]
            stringGen.append(books[i].title)
            stringGen.append(books[i].author)
            stringGen.append(books[i].isbn)
            stringGen.append(books[i].genre)
            stringGen.append(books[i].publisher)
            #print(books[i].publisher)
            stringGen.append(books[i].inventoryNumber)
            stringGen.append(books[i].state)
            listOfString.append(stringGen)

        return listOfString

#pres=BookPresenter()
#aux=pres.stringOfBooks()
#n=aux.__len__()

#for i in range(n):
 #   for j in range(7):
  #      print(aux[i][j]+' ')
   # print('\n')
        

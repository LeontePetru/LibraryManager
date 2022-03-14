
from BooksInventory import BooksInventory


class BookPresenter:

    def __init__(self):
        self.__bookInventory=BooksInventory()
        
        self.__bookData=self.stringOfBooks()

        self.__n = self.__bookData.__len__()
        
        self.__genres = []
        self.__genres.append("genre")
        self.__states = []
        self.__states.append("status")
        self.__states.append("available")
        self.__states.append("borrowed")
        self.__publishers = []
        self.__publishers.append("publisher")
        self.__authors = []
        self.__authors.append("author")

        for i in range(self.__n):
            if self.__bookData[i][3] not in self.__genres:
                self.__genres.append(self.__bookData[i][3])
            # if bookData[i][6] not in states:
            #   states.append(bookData[i][6])
            if self.__bookData[i][4] not in self.__publishers:
                self.__publishers.append(self.__bookData[i][4])
            if self.__bookData[i][1] not in self.__authors:
                self.__authors.append(self.__bookData[i][1])

    @property
    def bookInventory(self):
        return self.__bookInventory

    @bookInventory.setter
    def bookInventory(self, bookInventory):
        self.__bookInventory = bookInventory

    @property
    def bookData(self):
        return self.__bookData

    @bookData.setter
    def bookData(self, bookData):
        self.__bookData = bookData

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        self.__genres = genres

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, states):
        self.__states = states

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def publishers(self):
        return self.__publishers

    @publishers.setter
    def publishers(self, publishers):
        self.__publishers = publishers

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

    def sortedListOfStrings(self,sortStates):
        sortedBookData=[]

        for i in range (self.__n):
            if ((self.__bookData[i][3] == sortStates[0] or sortStates[0] == 'genre') and
                    (self.__bookData[i][6] == sortStates[1] or sortStates[1] == 'status') and
                    (self.__bookData[i][4] == sortStates[2] or sortStates[2] == 'publisher') and
                    (self.__bookData[i][1] == sortStates[3] or sortStates[3] == 'author')):
                sortedBookData.append(self.__bookData[i])
        return sortedBookData

    def nameSortedListOfStrings(self,name):
        sortedBookData1=[]

        for i in range(self.__n):
            aux=self.__bookData[i][0]
            if aux.lower() == name.lower():
                sortedBookData1.append(self.__bookData[i])

        return sortedBookData1
    #def ()

pres=BookPresenter()
#aux=pres.stringOfBooks()
#n=aux.__len__()

#for i in range(n):
 #   for j in range(7):
  #      print(aux[i][j]+' ')
   # print('\n')


#print(pres.bookData)
#print(pres.publishers)
#print(pres.states)
#print(pres.authors)
#print(pres.genres)
#a="sdsfsdSDDSDdsa"

#print(a.lower())


print(pres.nameSortedListOfStrings('Amintiri din copilarie52'))
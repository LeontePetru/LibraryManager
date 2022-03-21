import json
from Books import Book
from Users import LoggedUser

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

    def searchByNumber(self,number):
        bookList=self.read()
        n = bookList.__len__()
        for i in range(n):
            if(bookList[i].inventoryNumber==number):
                return bookList[i]
        return False

class LoggedUserPersistance(JSONPersist):
    def __init__(self,file):
        super().__init__(file)

    def read(self):
        data = self.deserialize()
        splitted = data.split('}')
        n = splitted.__len__()

        userList = []

        for i in range(n - 1):
            auxData = json.loads(splitted[i] + "}")
            auxBook = LoggedUser(auxData['_LoggedUser__username'], auxData['_LoggedUser__password'], auxData['_LoggedUser__role'])
            userList.append(auxBook);

        return userList

    def deleteUser(self, username):
        userList = self.read()
        newUserList = []
        n = userList.__len__()
        for i in range(n):
            if userList[i].username != username:
                newUserList.append(userList[i])
        self.serializeList(newUserList)
        return True

    def searchByUsername(self, username):
        userList = self.read()
        n = userList.__len__()
        for i in range(n):
            if (userList[i].username == username):
                return userList[i]
        return False

    def insertUser(self,user):
        userList=self.read()
        userList.append(user)
        self.serializeList(userList)






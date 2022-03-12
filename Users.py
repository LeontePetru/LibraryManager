class User:
    pass

class LoggedUser(User):

    def __init__(self,id,username,password):
        self.__id=id
        self.__username=username
        self.__password=password

class BookKeeper(LoggedUser):
    pass

class Admin(BookKeeper):
    pass

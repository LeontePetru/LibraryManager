from JSONPersistence import LoggedUserPersistance

class UserPresenter:

    def __init__(self):
        self.__userPersistance=LoggedUserPersistance("users.json")
        self.__users=self.__userPersistance.read()

    @property
    def users(self):
        return self.__users

    @users.setter
    def states(self, users):
        self.__users = users

    def stringOfUsers(self):
        listOfString= []
        users=self.users
        n=users.__len__()

        for i in range(n):
            stringGen=[]
            stringGen.append(users[i].username)
            stringGen.append(users[i].password)
            stringGen.append(users[i].role)

            listOfString.append(stringGen)

        return listOfString
from .User import User
class Admin(User):
    """! The Customer class
    Defines Customer class for customer users
    """
    nextID = 1000
    def __init__(self, userName, password):
        super().__init__(userName,password)       
        self.__userId = Admin.nextID
        self.__loginStatus = False
        self.__role = "admin"
        Admin.nextID += 1
        
    @property
    def userId(self):
        return self.__userId
    @property
    def role(self):
        return self.__role
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus):
        self.__loginStatus = loginStatus


    def adminInfo(self):
        return self.role + " user: " + self.userName  
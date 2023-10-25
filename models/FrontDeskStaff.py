from .User import User
class FrontDeskStaff(User):
    """! The FrontDeskStaff class
    Defines FrontDeskStaff class for FrontDeskStaff users
    """
    nextID = 2000
    def __init__(self, userName, password):
        super().__init__(userName,password)       
        self.__userId = FrontDeskStaff.nextID
        self.__loginStatus = False
        self.__role = "staff"
        FrontDeskStaff.nextID += 1
        
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


    def staffInfo(self):
        print(str(self.staffId) + " " + self.userName + " " )
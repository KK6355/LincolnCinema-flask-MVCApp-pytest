from .User import User
class Customer(User):
    """! The Customer class
    Defines Customer class for customer users
    """
    nextID = 3000
    def __init__(self, userName, password):
        super().__init__(userName,password)       
        self.__userId = Customer.nextID
        self.__loginStatus = False
        self.__role = "customer"
        Customer.nextID += 1
        self.bookingList = []
        self.notificationList = []
        self.couponList = []
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


    def customerInfo(self):
        print(str(self.userId) + " " + self.userName + " " )
    


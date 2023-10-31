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
        self.__bookingList = []
        self.__notificationList = []
        self.__couponList = []
        self.__cardList  = []
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
    @property
    def cardList(self):
        return self.__cardList
    @cardList.setter
    def cardList(self, cardList):
        self.__cardList = cardList
    @property
    def couponList(self):
        return self.__couponList
    @couponList.setter
    def couponList(self, couponList):
        self.__couponList= couponList
    @property
    def bookingList(self):
        return self.__bookingList
    @bookingList.setter
    def bookingList(self, bookingList):
        self.__bookingList = bookingList
    @property
    def notificationList(self):
        return self.__notificationList
    @notificationList.setter
    def notificationList(self, notificationList):
        self.__notificationList = notificationList
    def customerInfo(self):
        return self.role + " user: " + self.userName
    


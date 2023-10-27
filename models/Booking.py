
from datetime import datetime
class Booking:
    """! The Ticket class
    Defines class for movie tickets
    """
    nextRefNum = 8000
    def __init__(self, screenId,customerId):
        self.__refNum = Booking.nextRefNum
        self.__seatList = []
        self.__screenId = screenId
        #self.__payment = 0
        self.__payStatus = "unpaid"
        self.__customerId = customerId
        self.__createdOn = datetime.now()
        Booking.nextRefNum += 1
    
    @property
    def refNum(self):
        return self.__refNum
    @property
    def seatList(self):
        return self.__seatList
    @property
    def customerId(self):
        return self.__customerId
    @property
    def screenId(self):
        return self.__screenId
    @property
    def payStatus(self):
        return self.__payStatus
    @payStatus.setter
    def payStatus(self, status):
        self.__payStatus = status
    @property
    def createdOn(self):
        return self.__createdOn   
    # @property
    # def payment(self):
    #     return self.__payment
   
    # def getPrice(self, discount):
    #     return self.__price * (1-discount)
    def bookingInfo(self):
        print(f"Ticket Number:{self.refNum}, ticket price:{self.price}, ticket status:{self.payStatus}")
    # def takeSeat(self, seat:Seat) -> None:
    #     """! The method check if the seat is available, if so take the seat for the ticket and make seat unavailable for others
    #      Otherwise, throw an error when book a ticket .
    #     @param seat object
    #     @return None
    #     """
    #     pass
    # #combine screenId and seatId to determin if the seat is available
    # def offSeat(self, seat:Seat) -> None:
    #     """! Make the seat available for others.
    #     @param seat object
    #     @return None
    #     """
    #     pass
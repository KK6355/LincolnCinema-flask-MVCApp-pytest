class Seat:
    """! The Seat class
    Defines class for cinema seats
    """
    nextId = 100
    def __init__(self,seatRow,seatNum, hallId, price):
        self.__seatId = Seat.nextId
        Seat.nextId += 1
        self.__seatRow = seatRow
        self.__seatNum = seatNum
        self.__hallId = hallId
        self.__isAvailable = True
        self.__price = price
        
    @property
    def seatId(self):
        return self.__seatId
    @property
    def seatRow(self):
        return self.__seatRow
    @property
    def seatNum(self):
        return self.__seatNum
    @property
    def hallId(self):
        return self.__hallId
    @property
    def price(self):
        return self.__price
    @property
    def isAvailable(self):
        return self.__isAvailable
    @isAvailable.setter
    def isAvailable(self, isAvailable):
        self.__isAvailable = isAvailable

    def seatInfo(self):
        print(f"Seat: row{self.seatRow} number{self.seatNum}, Hall: {self.hallId}, Seat is available: {self.isAvailable}")

class Hall:
    """! The Hall class
    Defines class for four halls in cinema
    """
    nextId = 1
    def __init__(self, name, capacity):
        self.__hallId = Hall.nextId
        Hall.nextId += 1
        self.__name = name
        self.__capacity = capacity
        self.seatList = [] 
    @property
    def hallId(self):
        return self.__hallId
    @property
    def name(self):
        return self.__name
    @property
    def capacity(self):
        return self.__capacity
    
    def hallInfo(self):
        print(f"Hall Id: {self.hallId},hall name: {self.name}, hall capacity:{self.capacity}")
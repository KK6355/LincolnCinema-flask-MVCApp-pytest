class Hall:
    """! The Hall class
    Defines class for four halls in cinema
    """
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
        self.seatList = [] 
    
    @property
    def name(self):
        return self.__name
    @property
    def capacity(self):
        return self.__capacity
    
    def hallInfo(self):
        print(f"Hall number: {self.hallId}, hall capacity:{self.capacity}")
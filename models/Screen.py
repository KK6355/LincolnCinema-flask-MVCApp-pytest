class Screen:
    """! The Screen class
    Defines class for movie Screens(schedules)
    """
    nextId = 5000
    def __init__(self, movieId, hallId, scheduledDate, scheduledTime):
        self.__screenId =  Screen.nextId
        self.__movieId = movieId
        self.__hallId = hallId
        self.__scheduledDate = scheduledDate
        self.__scheduledTime = scheduledTime
        Screen.nextId += 1
        # self.screenList = []
        # self.availableSeats = []
        # self.unavailableSeats = []
    
    @property
    def screenId(self):
        return self.__screenId
    @property
    def movieId(self):
        return self.__movieId
    @property
    def hallId(self):
        return self.__hallId
    @property
    def scheduledDate(self):
        return self.__scheduledDate 
    @property
    def scheduledTime(self):
        return self.__scheduledTime 
    
    def screenInfo(self):
        print(f"screen Id: {self.screenId}, screen movie id: {self.movieId}, screen hall id: {self.hallId}, scheduled time: {self.scheduledTime}")
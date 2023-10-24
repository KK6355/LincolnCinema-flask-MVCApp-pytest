from abc import ABC, abstractmethod
class User(ABC):
    """! The User class
    Defines abstract class for all system users
    """
    def __init__(self, userName,password):     
        self._userName = userName
        self._password = password
       
        self._loginStatus = False
    @property
    def userName(self):
        return self._userName
    @property
    def password(self):
        return self._password
  
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus):
        self.__loginStatus = loginStatus
    # @abstractmethod 
    # def login(self):
    #     pass  
    # @abstractmethod 
    # def register(self):
    #     pass
class DebitCard:
    def __init__(self,cardNum, holderName,type):
        self.__paymethod = "debitCard"
        self.__cardNum = cardNum
        self.__holderName = holderName
        self.__type = type
        self.__balance = 1000
    @property
    def paymethod(self):
        return self.__paymethod
    @property
    def cardNum(self):
        return self.__cardNum
    @property
    def holderName(self):
        return self.__holderName
    @property
    def type(self):
        return self.__type
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance
   
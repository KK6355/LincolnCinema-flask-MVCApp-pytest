class CreditCard:
    def __init__(self,cardNum, holderName,type,expiration):
        self.__paymethod = "creditCard"
        self.__cardNum = cardNum
        self.__holderName = holderName
        self.__type = type
        self.__expiration = expiration
    @property
    def cardNum(self):
        return self.__cardNum
    @property
    def paymethod(self):
        return self.__paymethod
    @property
    def holderName(self):
        return self.__holderName
    @property
    def type(self):
        return self.__type
    @property
    def expiration(self):
        return self.__expiration
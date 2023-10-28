class Coupon:
    nextId = 9000
    def __init__(self,customerId, expiryDate,discount):
        self.__couponId = Coupon.nextId
        Coupon.nextId += 1
        self.__customerId = customerId
        self.__expiryDate = expiryDate
        self.__discount = discount
        self.__status = "unused"
    @property
    def couponId(self):
        return self.__couponId
    @property
    def customerId(self):
        return self.__customerId
    @property
    def expiryDate(self):
        return self.__expiryDate
    @property
    def discount(self):
        return self.__discount
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,status):
        self.__status = status
    def __str__(self):
        return f"Coupon:{self.couponId}, expire at: {self.expiryDate}, discount: {self.discount*100}%"
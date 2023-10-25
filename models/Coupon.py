class Coupon:
    nextId = 9000
    def __init__(self,expiryDate,discount):
        self.__couponId = Coupon.nextId
        Coupon.nextId += 1
        self.__expiryDate = expiryDate
        self.__discount = discount
    @property
    def couponId(self):
        return self.__couponId
    @property
    def expiryDate(self):
        return self.__expiryDate
    @property
    def discount(self):
        return self.__discount
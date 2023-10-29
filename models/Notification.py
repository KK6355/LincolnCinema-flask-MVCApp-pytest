from datetime import datetime
class Notification:
    nextId = 10000
    def __init__(self,category,content):
        self.__notificationId = Notification.nextId
        Notification.nextId += 1
        self.__createdOn = datetime.now()
        self.__category  = category
        self.__content = content
    @property
    def notificationId(self):
        return self.__notificationId
    @property
    def category(self):
        return self.__category
    @property
    def createdOn(self):
        return self.__createdOn
    @property
    def content(self):
        return self.__content
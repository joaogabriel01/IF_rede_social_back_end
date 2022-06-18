class LoginDto:
    def __init__(self,nickname="", password=""):
        self.__nickname = nickname
        self.__password = password

    def getNickname(self):
        return self.__nickname
    
    def getPassword(self):
        return self.__password

    def setNickname(self,nickname):
        self.__nickname = nickname
    
    def setPassword(self,password):
        self.__password = password

class Create:
    def __init__(self,nickname="",mail="",password="", confirmPassword=""):
        self.__nickname = nickname
        self.__mail = mail
        self.__password = password
        self.__confirmPassword = confirmPassword
        

    def getNickname(self):
        return self.__nickname
    
    def getPassword(self):
        return self.__password
    
    def getMail(self):
        return self.__mail

    def getConfirmPassword(self):
        return self.__confirmPassword

    def setNickname(self,nickname):
        self.__nickname = nickname
    
    def setPassword(self,password):
        self.__password = password
    
    def setMail(self,mail):
        self.__mail = mail

    def setConfirmPassword(self, confirmPassword):
        self.__confirmPassword = confirmPassword
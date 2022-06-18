class ResetPasswordDto:
    def __init__(self,id="", newPassword=""):
        self.__id = id
        self.__newPassword = newPassword

    def getId(self):
        return self.__id
    
    def getNewPassword(self):
        return self.__newPassword

    def setId(self,id):
        self.__id = id
    
    def setNewPassword(self,newPassword):
        self.__newPassword = newPassword

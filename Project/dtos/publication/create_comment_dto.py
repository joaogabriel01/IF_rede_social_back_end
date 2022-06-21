class CreateCommentDto:
    def __init__(self,nickname,idPublication,text,idUser=0):
        self.__nickname = nickname
        self.__idPublication = idPublication
        self.__text = text

    def getNickname(self):
        return self.__nickname

    def getIdUser(self):
        return self.__idUser
    
    def getIdPublication(self):
        return self.__idPublication

    def getText(self):
        return self.__text
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setNickname(self,nickname):
        self.__nickname = nickname

    def setIdPublication(self, idPublication):
        self.__idPublication = idPublication
    
    def setText(self, text):
        self.__text = text

   
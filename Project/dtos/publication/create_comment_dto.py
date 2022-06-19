class CreateCommentDto:
    def __init__(self,idUser,idPublication,text):
        self.__idUser = idUser
        self.__idPublication = idPublication
        self.__text = text

    def getIdUser(self):
        return self.__idUser
    
    def getIdPublication(self):
        return self.__idPublication

    def getText(self):
        return self.__text
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setIdPublication(self, idPublication):
        self.__idPublication = idPublication
    
    def setText(self, text):
        self.__text = text

   
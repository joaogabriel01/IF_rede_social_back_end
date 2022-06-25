class LikePublicationDto:
    def __init__(self,idPublication,idUser=0):
        self.__idUser = idUser
        self.__idPublication = idPublication

    def getIdUser(self):
        return self.__idUser
    
    def getIdPublication(self):
        return self.__idPublication
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setIdPublication(self, idPublication):
        self.__idPublication = idPublication


   
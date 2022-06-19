class CreateDto:
    def __init__(self,idUser,text,images):
        self.__idUser = idUser
        self.__text = text
        self.__images = images

    def getIdUser(self):
        return self.__idUser
    
    def getText(self):
        return self.__text

    def getImages(self):
        return self.__images
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setText(self, text):
        self.__text = text
    
    def setImages(self, images):
        self.__images = images

   
class CreateDto:
    def __init__(self,idUser,idGroup,text,images):
        self.__idUser = idUser
        self.__idGroup = idGroup
        self.__text = text
        self.__images = images

    def getIdUser(self):
        return self.__idUser
    
    def getIdGroup(self):
        return self.__idGroup
    
    def getText(self):
        return self.__text

    def getImages(self):
        return self.__images
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setIdGroup(self,idGroup):
        self.__idGroup = idGroup

    def setText(self, text):
        self.__text = text
    
    def setImages(self, images):
        self.__images = images

   
class CreateDto:
    def __init__(self,groupName,text,images,tags,idUser=0,idGroup=0):
        self.__idUser = idUser
        self.__idGroup = idGroup
        self.__groupName = groupName
        self.__text = text
        self.__images = images
        self.__tags = tags
    
    def getGroupName(self):
        return self.__groupName

    def getIdUser(self):
        return self.__idUser
    
    def getIdGroup(self):
        return self.__idGroup
    
    def getText(self):
        return self.__text

    def getImages(self):
        return self.__images

    def getTags(self):
        return self.__tags

    def setGroupName(self,groupName):
        self.__groupName = groupName        
    
    def setIdUser(self,idUser):
        self.__idUser = idUser

    def setIdGroup(self,idGroup):
        self.__idGroup = idGroup

    def setText(self, text):
        self.__text = text
    
    def setImages(self, images):
        self.__images = images

    def setTags(self, tags):
        self.__tags = tags

   
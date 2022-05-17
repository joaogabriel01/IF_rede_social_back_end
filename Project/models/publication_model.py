class Publication:
    def __init__(self,id_user,description,images=0,id=0):
        self.__id = id
        self.__id_user = id_user
        self.__description = description
        self.__images = images
        

    def getId(self):
        return self.__id

    def getIdUser(self):
        return self.__id_user
    
    def getDescription(self):
        return self.__description

    def getImages(self):
        return self.__images
    
    def setId(self,id):
        self.__id = id
    
    def setIdUser(self,idUser):
        self.__id_user = idUser

    def setDescription(self, description):
        self.__description = description
    
    def setImages(self, images):
        self.__images = images

   
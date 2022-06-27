class GroupDto:
    def __init__(self,id=0,name="",description="",idUser=0):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__idUser = idUser

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description
    
    def getIdUser(self):
        return self.__idUser

    def setId(self,id):
        self.__id = id
    
    def setName(self,name):
        self.__name = name

    def setDescription(self,description):
        self.__description = description

    def setIdUser(self,idUser):
        self.__idUser = idUser


   
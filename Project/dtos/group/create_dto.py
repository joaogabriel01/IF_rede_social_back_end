class GroupDto:
    def __init__(self,id=0,name="",idUser=0):
        self.__id = id
        self.__name = name
        self.__idUser = idUser

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getIdUser(self):
        return self.__idUser

    def setId(self,id):
        self.__id = id
    
    def setName(self,name):
        self.__name = name

    def setIdUser(self,idUser):
        self.__idUser = idUser


   
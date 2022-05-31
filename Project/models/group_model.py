class Group:
    def __init__(self,id_group="",name="",users=[]):
        self.__id_group = id_group
        self.__name = name
        self.__users = users

    def getId(self):
        return self.__id_group

    def getName(self):
        return self.__name
    
    def getUsers(self):
        return self.__users
    
    def setId(self,id):
        self.__id_group = id
    
    def setName(self,name):
        self.__name = name

    def setUsers(self,users):
        self.__users = users

   
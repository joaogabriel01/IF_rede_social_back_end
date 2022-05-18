class User:
    def __init__(self,nickname="",mail="",password="",id=0):
        self.__id = id
        self.__nickname = nickname
        self.__mail = mail
        self.__password = password
        

    def getId(self):
        return self.__id

    def getNickname(self):
        return self.__nickname
    
    def getPassword(self):
        return self.__password
    
    def getMail(self):
        return self.__mail

    def setId(self,id):
        self.__id = id

    def setNickname(self,nickname):
        self.__nickname = nickname
    
    def setPassword(self,password):
        self.__password = password
    
    def setMail(self,mail):
        self.__mail = mail
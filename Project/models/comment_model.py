class Comment:
    def __init__(self,id_comment="",id_user="",id_publication="",content=""):
        self.__id_comment = id_comment
        self.__id_user = id_user
        self.__id_publication = id_publication
        self.__content = content
        

    def getId(self):
        return self.__id_comment

    def getIdUser(self):
        return self.__id_user
    
    def getIdPublication(self):
        return self.__id_publication

    def getContent(self):
        return self.__content
    
    def setId(self,id):
        self.__id_comment = id
    
    def setIdUser(self,idUser):
        self.__id_user = idUser

    def setPublication(self, idPublication):
        self.__id_publication = idPublication
    
    def setContent(self, content):
        self.__content = content

   
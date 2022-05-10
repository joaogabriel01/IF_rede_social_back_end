from ..daos.user_dao import UserDao
from ..models.user_model import User


class UserController:

    def __init__(self,db):
        self.__db = db
        self.__userDao = UserDao(self.__db)

    def checkNickname(self,nickname):
        dados = self.__userDao.findByNickname(nickname)
        return dados

    def checkEmail(self,email):
        dados = self.__userDao.findByEmail(email)
        return dados

    def confirmPassword(self,password, passwordConfirm):
        if(password == passwordConfirm):
            return True

    def saveUser(self,userPost):
        if( not (self.checkEmail(userPost['email']) is None)):
            return {"response": "Email já existente"}
        if( not (self.checkNickname(userPost['nickname']) is None)):
            return {"response": "Usuário já existente"}
        if( not (self.confirmPassword(userPost['password'],userPost['password-confirm']))):
            return {"response": "Senhas não correspondem"}
        user = User(userPost['nickname'],userPost['email'],userPost['password'])
        self.__userDao.save(user)
        return {"response": "Usuário criado com sucesso"}

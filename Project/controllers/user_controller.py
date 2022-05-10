from ..daos.user_dao import UserDao
from ..models.user_model import User
import json


class UserController:

    def __init__(self, db):
        self.__db = db
        self.__userDao = UserDao(self.__db)

    def checkNickname(self, nickname):
        dados = self.__userDao.findByNickname(nickname)
        return dados

    def checkEmail(self, email):
        dados = self.__userDao.findByEmail(email)
        return dados

    def confirmPassword(self, password, passwordConfirm):
        if(password == passwordConfirm):
            return True

    def saveUser(self, userPost):
        if( not (self.checkEmail(userPost['email']) is None)):
            return {"response": "Email já existente"}
        if( not (self.checkNickname(userPost['nickname']) is None)):
            return {"response": "Usuário já existente"}
        if( not (self.confirmPassword(userPost['password'],userPost['password-confirm']))):
            return {"response": "Senhas não correspondem"}
        user = User(userPost['nickname'],userPost['email'],userPost['password'])
        self.__userDao.save(user)
        return {"response": "Usuário criado com sucesso"}

    def sendEmailToResetPassword(self, email):
        if( self.checkEmail(email) is None):
            return {"response": "Email não existe"}
        return {"response": "Email para resetar a senha enviado"}

    def resetPassword(self, data):
        self.__userDao.updatePassword(data['id-user'], data['password'])
        dataUser = self.__userDao.findById(data['id-user'])
        user = User(dataUser[1],dataUser[2],dataUser[3],dataUser[0])
        response = json.dumps(user.__dict__)
        return response

from ..daos.user_dao import UserDao
from ..models.user_model import User
from ..ext.send_email import SendEmail
import json
import uuid
import cryptocode
import os
from dotenv import load_dotenv

load_dotenv()

class UserController:

    def __init__(self, db):
        self.__db = db
        self.__userDao = UserDao(self.__db)

    def checkNickname(self, nickname):
        data = self.__userDao.findByNickname(nickname)
        return data

    def checkEmail(self, email):
        data = self.__userDao.findByEmail(email)
        return data

    def confirmPassword(self, password, passwordConfirm):
        if(password == passwordConfirm):
            return True

    def checkUiid(self, uuid):
        data = self.__userDao.findByUuid
        if(data is None):
            return True
        return False

    
    def saveUser(self, userPost):
        if( not (self.checkEmail(userPost['email']) is None)):
            return {"response": "Email já existente"}
        if( not (self.checkNickname(userPost['nickname']) is None)):
            return {"response": "Usuário já existente"}
        if( not (self.confirmPassword(userPost['password'],userPost['password-confirm']))):
            return {"response": "Senhas não correspondem"}
        id = uuid.uuid4()
        encryptedPassword = cryptocode.encrypt(userPost['password'],os.getenv("CRYPTOGRAPHY_HASH"))
        user = User(nickname=userPost['nickname'],mail=userPost['email'],password=encryptedPassword, id=id)
        self.__userDao.save(user)
        return {"response": "Usuário criado com sucesso"}

    def loginUser(self, userPost):
        return 1

    def sendEmailToResetPassword(self, email):
        if( self.checkEmail(email) is None):
            return {"response": "Email não existe"}
        body_teste = "<p>Oi estou apenas testando uma coisa<p>"
        subject_teste = "teste"
        SendEmail.send_email(body_teste, subject_teste, email)
        return {"response": "Email para resetar a senha enviado"}

    def resetPassword(self, data):
        encryptedPassword = cryptocode.encrypt(data['password'],os.getenv("CRYPTOGRAPHY_HASH"))
        self.__userDao.updatePassword(data['uuid_user'], encryptedPassword)
        dataUser = self.__userDao.findByUuid(data['uuid_user'])
        user = User(nickname=dataUser[1],mail=dataUser[2],password=encryptedPassword,id=dataUser[0])
        response = json.dumps(user.__dict__)
        return response

from ..daos.user_dao import UserDao
from ..models.user_model import User
from ..ext.send_email import SendEmail
import json
import uuid
import bcrypt
import os
from dotenv import load_dotenv
import datetime
import jwt
from flask import jsonify

load_dotenv()

class UserController:

    def __init__(self, db):
        self.__db = db
        self.__userDao = UserDao(self.__db)

    def checkNickname(self, nickname):
        data = self.__userDao.findByNickname(nickname)
        return data

    def checkId(self, id):
        data = self.__userDao.findById(id)
        print(data)
        if (data is None):
            return False
        return True

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
        try:
            if(self.checkEmail(userPost['email'])):
                return jsonify({"response": "Email já existente"}), 409
            if(self.checkNickname(userPost['nickname'])):
                return jsonify({"response": "Usuário já existente"}), 409
            if(not self.confirmPassword(userPost['password'],userPost['password-confirm'])):
                return jsonify({"response": "Senhas não correspondem"}), 409
        
            id = uuid.uuid4()
            encryptedPassword = bcrypt.hashpw((userPost['password']).encode('utf-8'),bcrypt.gensalt())
            print(bcrypt.gensalt())
            user = User(nickname=userPost['nickname'],mail=userPost['email'],password=encryptedPassword, id=id)
            self.__userDao.save(user)
            return jsonify({"response": "Usuário criado com sucesso"}), 201
        except:
            return jsonify({"response":"Houve um problema em sua requsição"}), 400

    def loginUser(self, userPost):
        try:
            uuidUser = self.__userDao.findByNickname(userPost['nickname'])
            if(uuidUser is not None):
                passwordHash = self.__userDao.findByUuid(uuidUser)[3].encode('utf-8')

                payload = {
                    "id": uuidUser,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                }

                token = jwt.encode(payload, os.getenv('CRYPTOGRAPHY_HASH'))
                if(bcrypt.checkpw(userPost['password'].encode('utf-8'),passwordHash)):
                    return jsonify({"response": "Usuário autenticado","token": token}), 202
            return jsonify({"response": "Usuário não autenticado"}), 401
        except:
            return jsonify({"response":"Houve um problema em sua requsição"}), 400

    def sendEmailToResetPassword(self, email):
        try:
            if( self.checkEmail(email) is None):
                return jsonify({"response": "Email não existe"}), 404
            body_teste = "<p>Oi estou apenas testando uma coisa<p>"
            subject_teste = "teste"
            SendEmail.send_email(body_teste, subject_teste, email)
            return jsonify({"response": "Email para resetar a senha enviado"}), 200
        except:
            return jsonify({"response":"Houve um problema em sua requsição"}), 400

    def resetPassword(self, userPost):
        try:
            encryptedPassword = bcrypt.hashpw((userPost['password']).encode('utf-8'),bcrypt.gensalt())
            self.__userDao.updatePassword(userPost['uuid_user'], encryptedPassword)
            return jsonify({"response":"Senha alterada com sucesso"}), 200
        except:
            return jsonify({"response":"Houve um problema em sua requsição"}), 400

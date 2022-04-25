from ..daos.user_dao import UserDao
from ..models.user_model import User


class UserController:

    def __init__(self,db):
        self.__db = db


    def confirmPassword(self,password, passwordConfirm):
        if(password == passwordConfirm):
            return True
    
    def saveUser(self,userPost):
        if(self.confirmPassword(userPost['password'],userPost['password-confirm'])):
            user = User(userPost['nickname'],userPost['email'],userPost['password'])
            userDao = UserDao(self.__db)
            userDao.save(user)

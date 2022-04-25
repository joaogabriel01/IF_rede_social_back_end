from ..daos.user_dao import UserDao
from ..models.user_model import User

class UserController:
    
    def saveUser(self,db):
        user = User('joao','1234','ewdwef@.do')
        userDao = UserDao(db)
        userDao.save(user)
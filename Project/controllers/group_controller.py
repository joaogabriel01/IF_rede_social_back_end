from ..daos.group_dao import GroupDao
from ..models.group_model import Group
from ..controllers.user_controller import UserController

from flask import jsonify

class GroupController:

    def __init__(self, db):
        self.__db = db
        self.__groupDao = GroupDao(self.__db)
        self.__userController = UserController(self.__db)
        

    def save(self, groupPost):
 
            group = Group(name=groupPost['groupname'])
            self.__groupDao.save(group)
            
            return jsonify({"response":"Grupo criado com sucesso"}), 201



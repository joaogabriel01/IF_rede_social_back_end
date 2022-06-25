from ..daos.group_dao import GroupDao
from ..models.group_model import Group
from ..controllers.user_controller import UserController

from flask import jsonify

class GroupController:

    def __init__(self, db):
        self.__db = db
        self.__groupDao = GroupDao(self.__db)

    def checkName(self,name):
        data = self.__groupDao.findByName(name)
        return data

    def save(self, group):
        idGroup = self.checkName(group.getName())
        if(idGroup):
            return jsonify({"response": "Nome do grupo já está sendo utilizado"})
        self.__groupDao.save(group)  
        self.saveUser(group)
        return jsonify({"response":"Grupo criado com sucesso"}), 201

    def saveUser(self, userGroup):
        idGroup = self.checkName(userGroup.getName())
        if(not idGroup):
            return jsonify({"response":"Groupo não encontrado"})
        userGroup.setId(idGroup)
        self.__groupDao.saveUser(userGroup)
        return jsonify({"response":"Usuário inserido com sucesso"}), 201



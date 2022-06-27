from ..daos.group_dao import GroupDao
from ..models.group_model import Group
from ..controllers.user_controller import UserController

from flask import jsonify

class GroupController:

    def __init__(self, db):
        self.__db = db
        self.__groupDao = GroupDao(self.__db)

    def findIdByName(self,name):
        try:
            data = self.__groupDao.findIdByName(name)['id_group']
        except:
            return False
        return data

    def save(self, group):
        idGroup = self.findIdByName(group.getName())
        if(idGroup):
            return jsonify({"response": "Nome do grupo já está sendo utilizado"})
        self.__groupDao.save(group)  
        self.saveUser(group)
        return jsonify({"response":"Grupo criado com sucesso"}), 201

    def saveUser(self, userGroup):
        idGroup = self.findIdByName(userGroup.getName())
        if(not idGroup):
            return jsonify({"response":"Groupo não encontrado"})
        userGroup.setId(idGroup)
        self.__groupDao.saveUser(userGroup)
        return jsonify({"response":"Usuário inserido com sucesso"}), 201

    def getGroups(self, idUser):
        groups = self.__groupDao.getGroups()
        for group in groups:
            group['amI'] = False
            usersOfGroup = self.__groupDao.getUsersInGroup(group['id_group'])
            for user in usersOfGroup:
                if(idUser == user['id_user']):
                    group['amI'] = True
                    pass
        return jsonify(groups), 200



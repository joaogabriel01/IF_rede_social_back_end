from multiprocessing.sharedctypes import Value
from ..daos.publication_dao import PublicationDao
from ..controllers.user_controller import UserController
from ..controllers.group_controller import GroupController

from flask import jsonify

class PublicationController:

    def __init__(self, db):
        self.__db = db
        self.__publicationDao = PublicationDao(self.__db)
        self.__userController = UserController(self.__db)
        self.__groupController = GroupController(self.__db)
        
        

    def checkId(self, id):
        data = self.__publicationDao.findById(id)
        if (data is None):
            return False
        return True

    def savePublication(self, publication):
        try:
            idGroup = self.__groupController.checkName(publication.getGroupName())
            if(not(idGroup)):
                return jsonify({"response":"Grupo não encontrado"}), 404
            publication.setIdGroup(idGroup)
            self.__publicationDao.save(publication)
            return jsonify({"response":"Publicação criada com sucesso"}),201

        except ValueError:
            return jsonify({"response":"Houve um problema interno"}), 400
    
    def saveComment(self,comment):
        try:
            if(not(self.checkId(comment.getIdPublication()))):
                return jsonify({"response":"Publcação não encontrada"}), 404
            self.__publicationDao.saveComment(comment)
            return jsonify({"response":"Comentário criado com sucesso"}), 201
        except:
            return jsonify({"response":"Houve um problema interno"}), 400

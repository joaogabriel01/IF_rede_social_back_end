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
            idGroup = self.__groupController.findIdByName(publication.getGroupName())
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

    def likePublication(self, publication):
        try:
            self.__publicationDao.likePubication(publication)
            return jsonify({"response":"Sucesso ao dar like"}), 200
        except ValueError:
            return jsonify({"response":"Houve um problema interno"}), 400

    def getPublications(self, user):
        publications = self.__publicationDao.getPublications(user)
        for publication in publications:
            publication['date'] = publication['date'].strftime("%d/%m/%Y, %H:%M:%S")
            publication['tags'] = self.__publicationDao.getTagsPublications(publication['id_publication'])
        return jsonify(publications), 200

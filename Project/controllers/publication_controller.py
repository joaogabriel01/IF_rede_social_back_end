from ..daos.publication_dao import PublicationDao
from ..models.publication_model import Publication
from ..controllers.user_controller import UserController

from flask import jsonify

class PublicationController:

    def __init__(self, db):
        self.__db = db
        self.__publicationDao = PublicationDao(self.__db)
        self.__userController = UserController(self.__db)
        

    def checkId(self, id):
        data = self.__publicationDao.findById(id)
        print(data)
        if (data is None):
            return False
        return True

    def savePublication(self,publicationPost):
        try:
            if(not(self.__userController.checkId(publicationPost['idUser']))):
                return jsonify({"response":"Usuário não encontrado"}), 404
        
            publication = Publication(publicationPost['idUser'],publicationPost['text'],publicationPost['images'])
            self.__publicationDao.save(publication)
            return jsonify({"response":"Publicação criada com sucesso"}),201

        except:
            return jsonify({"response":"Houve um problema interno"}), 400

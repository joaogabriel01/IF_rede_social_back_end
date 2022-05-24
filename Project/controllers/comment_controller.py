from ..daos.comment_dao import CommentDao
from ..models.comment_model import Comment
from ..controllers.user_controller import UserController
from ..controllers.publication_controller import PublicationController
from flask import jsonify

class CommentController:

    def __init__(self, db):
        self.__db = db
        self.__comentDao = CommentDao(self.__db)
        self.__userController = UserController(self.__db)
        self.__publication_controller = PublicationController(self.__db)

    def saveComment(self,commentPost):
        try:
            if(not(self.__userController.checkId(commentPost['idUser']))):
                return jsonify({"response":"Usuário não encontrado"}), 404
            if(not(self.__publication_controller.checkId(commentPost['idPublication']))):
                return jsonify({"response":"Publcação não encontrada"}), 404
        
            comment = Comment(id_user=commentPost['idUser'],id_publication=commentPost['idPublication'],content=commentPost['content'])
            self.__comentDao.save(comment)
            
            return jsonify({"response":"Comentário criado com sucesso"}), 201
        except:
            return jsonify({"response":"Houve um problema interno"}), 400


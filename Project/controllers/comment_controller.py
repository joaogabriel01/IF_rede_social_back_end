from ..daos.comment_dao import CommentDao
from ..models.comment_model import Comment
from flask import jsonify

class CommentController:

    def __init__(self, db):
        self.__db = db
        self.__comentDao = CommentDao(self.__db)

    def saveComment(self,commentPost):
        comment = Comment(id_user=commentPost['idUser'],id_publication=commentPost['idPublication'],content=commentPost['content'])
        self.__comentDao.save(comment)
        
        return jsonify({"response":"Comentário criado com sucesso"}),201


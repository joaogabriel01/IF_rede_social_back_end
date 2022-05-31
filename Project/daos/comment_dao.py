SQL_CREATE_COMMENT = 'insert into comments(id_user,id_publication,content) values (%s,%s,%s)'

class CommentDao:

    def __init__(self,db):
        self.__db=db


    def save(self,comment):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_COMMENT, (comment.getIdUser(), comment.getIdPublication(), comment.getContent()))
        cursor._idPost = cursor.lastrowid
        self.__db.commit()
        return 1
    


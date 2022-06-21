SQL_CREATE_PUBLICATION = 'insert into publications(id_user, id_group, description) values (%s, %s, %s)'
SQL_CREATE_IMAGE = 'insert into images(url) values (%s)'
SQL_LINK_IMAGE_PUBLICATION = 'insert into publication_images(id_publication, id_image) values (%s, %s)'
SQL_FIND_BY_ID = 'select id_publication, id_user description from publications where id_publication = (%s)'

SQL_CREATE_COMMENT = 'insert into comments(id_user,id_publication,content) values (%s,%s,%s)'


class PublicationDao:

    def __init__(self,db):
        self.__db=db

    def findById(self, idPublication):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_ID, (idPublication,))
        data = cursor.fetchone()
        self.__db.commit()
        cursor.close()
        return data


    def save(self,publication):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_PUBLICATION, (publication.getIdUser(), publication.getIdGroup(), publication.getText()))
        cursor._idPost = cursor.lastrowid
        if(publication.getImages()!=''):
            for url_image in publication.getImages():
                cursor.execute(SQL_CREATE_IMAGE, (url_image,))
                cursor._idImage = cursor.lastrowid
                cursor.execute(SQL_LINK_IMAGE_PUBLICATION, (cursor._idPost, cursor._idImage))
        self.__db.commit()
        cursor.close()
        return 1

    def saveComment(self,comment):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_COMMENT, (comment.getIdUser(), comment.getIdPublication(), comment.getText()))
        cursor._idPost = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return 1
    
    


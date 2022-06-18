SQL_CREATE_PUBLICATION = 'insert into publications(id_user, description) values (%s, %s)'
SQL_CREATE_IMAGE = 'insert into images(url) values (%s)'
SQL_LINK_IMAGE_PUBLICATION = 'insert into publication_images(id_publication, id_image) values (%s, %s)'
SQL_FIND_BY_ID = 'select id_publication, id_user description from publications where id_publication = (%s)'


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
        cursor.execute(SQL_CREATE_PUBLICATION, (publication.getIdUser(), publication.getDescription()))
        cursor._idPost = cursor.lastrowid
        if(publication.getImages()!=0):
            for url_image in publication.getImages():
                cursor.execute(SQL_CREATE_IMAGE, (url_image,))
                cursor._idImage = cursor.lastrowid
                cursor.execute(SQL_LINK_IMAGE_PUBLICATION, (cursor._idPost, cursor._idImage))
        self.__db.commit()
        cursor.close()
        return 1
    


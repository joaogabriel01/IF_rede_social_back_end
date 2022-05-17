SQL_CREATE_PUBLICATION = 'insert into publications(id_user,description) values (%s,%s)'
SQL_CREATE_IMAGE = 'insert into images(url) values (%s)'
SQL_LINK_IMAGE_PUBLICATION = 'insert into publication_images(id_publication,id_image) values (%s,%s)'


class PublicationDao:

    def __init__(self,db):
        self.__db=db


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
        return 1
    


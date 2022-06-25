SQL_CREATE_PUBLICATION = 'insert into publications(id_user, id_group, description) values (%s, %s, %s)'
SQL_CREATE_IMAGE = 'insert into images(url) values (%s)'
SQL_LINK_IMAGE_PUBLICATION = 'insert into publication_images(id_publication, id_image) values (%s, %s)'
SQL_FIND_BY_ID = 'select id_publication, id_user description from publications where id_publication = (%s)'
SQL_CREATE_TAG = 'insert into tags(text) values (%s)'
SQL_LINK_TAG_PUBLICATION = 'insert into publications_tags(id_publication, id_tag) values (%s,%s)'
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
        try:
            cursor.execute(SQL_CREATE_PUBLICATION, (publication.getIdUser(), publication.getIdGroup(), publication.getText()))
            cursor._idPublic = cursor.lastrowid
            for url_image in publication.getImages():
                idImage = self.saveImages(cursor,url_image)
                self.insertImagePublication(cursor,idImage)
            
            for tag in publication.getTags():
                idTag = self.saveTag(cursor,tag)
                self.insertTagPublication( cursor, idTag)
            self.__db.commit()
            cursor.close()
        except:
            self.__db.rollback()
            cursor.close()
            return False;

        return True

    def saveComment(self,comment):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_COMMENT, (comment.getIdUser(), comment.getIdPublication(), comment.getText()))
        cursor._idPost = cursor.lastrowid
        return True

    def insertImagePublication(self,cursor, id_image):
        cursor.execute(SQL_LINK_IMAGE_PUBLICATION, (cursor._idPublic, id_image))
        return True

    def saveTag(self, cursor, tag):
        cursor.execute(SQL_CREATE_TAG, (tag))
        cursor._idTag = cursor.lastrowid
        return cursor._idTag

    def saveImages(self,cursor, images):
        cursor.execute(SQL_CREATE_IMAGE, (images))
        cursor._idImages = cursor.lastrowid
        return cursor._idImages

    def insertTagPublication(self, cursor, id_tag):
        cursor.execute(SQL_LINK_TAG_PUBLICATION, (cursor._idPublic, id_tag))
        return True

    
    


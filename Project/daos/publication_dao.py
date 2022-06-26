SQL_CREATE_PUBLICATION = 'insert into publications(id_user, id_group, content) values (%s, %s, %s)'
SQL_CREATE_IMAGE = 'insert into images(url) values (%s)'
SQL_LINK_IMAGE_PUBLICATION = 'insert into publication_images(id_publication, id_image) values (%s, %s)'
SQL_FIND_BY_ID = 'select id_publication, id_user content from publications where id_publication = (%s)'
SQL_CREATE_TAG = 'insert into tags(text) values (%s)'
SQL_LINK_TAG_PUBLICATION = 'insert into publications_tags(id_publication, id_tag) values (%s,%s)'
SQL_CREATE_COMMENT = 'insert into comments(id_user,id_publication,content) values (%s,%s,%s)'
SQL_LIKE_PUBLICATION = 'insert into likes (id_user, id_publication) values (%s,%s)'
SQL_GET_PUBLICATIONS = 'select s.id_publication,s.group_name,s.date,s.content,s.likes from search_publications s inner join groups_network gn on gn.id_group = s.id_group inner join users_groups ug on ug.id_group = gn.id_group where ug.id_user = %s'
SQL_GET_TAGS_PUBLICATIONS = 'select t.text from tags t inner join publications_tags pt on pt.id_tag = t.id_tag where pt.id_publication = %s'

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
        self.__db.commit()
        cursor.close()
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

    def likePubication(self, publication):
        cursor = self.__db.cursor()
        cursor.execute(SQL_LIKE_PUBLICATION, (publication.getIdUser(), publication.getIdPublication()))
        self.__db.commit()
        cursor.close()
        return True

    def getPublications(self, idUser):
        cursor = self.__db.cursor()
        cursor.execute(SQL_GET_PUBLICATIONS, (idUser))
        self.__db.commit()
        publications = cursor.fetchall()
        cursor.close()
        return publications
    
    def getTagsPublications(self, idPublication):
        cursor = self.__db.cursor()
        cursor.execute(SQL_GET_TAGS_PUBLICATIONS, (idPublication))
        self.__db.commit()
        tags = cursor.fetchall()
        cursor.close()
        return tags
    
    


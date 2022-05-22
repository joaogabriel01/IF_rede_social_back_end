from ..daos.publication_dao import PublicationDao
from ..models.publication_model import Publication

class PublicationController:

    def __init__(self, db):
        self.__db = db
        self.__publicationDao = PublicationDao(self.__db)

    def savePublication(self,publicationPost):
        publication = Publication(publicationPost['idUser'],publicationPost['text'],publicationPost['images'])
        self.__publicationDao.save(publication)
        
        return {"response":"Publicação criada com sucesso"}
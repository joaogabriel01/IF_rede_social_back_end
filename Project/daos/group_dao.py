SQL_CREATE_GROUP = 'insert into groups_network(name) values (%s)'
SQL_CREATE_PUBLICATION = 'insert into publications(id_user, description) values (%s, %s)'

class GroupDao:

    def __init__(self,db):
        self.__db=db

    def save(self, group):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_GROUP, (group.getName()))
        cursor._idGroup = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return 1
SQL_CREATE_GROUP = 'insert into groups_network(name) values (%s)'
SQL_FIND_BY_NAME = 'select id_group from groups_network where name like %s'

class GroupDao:

    def __init__(self,db):
        self.__db=db

    def findByName(self, name):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_NAME, (name,))
        data = cursor.fetchone()
        self.__db.commit()
        cursor.close()
        return data

    def save(self, group):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_GROUP, (group.getName()))
        cursor._idGroup = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return 1
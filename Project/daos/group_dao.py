SQL_CREATE_GROUP = 'insert into groups_network(name) values (%s)'
SQL_FIND_BY_NAME = 'select id_group from groups_network where name like %s'
SQL_INSERT_USER = 'insert into users_groups (id_user, id_group) values (%s,%s)'

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

    def saveUser(self, groupUser):
        cursor = self.__db.cursor()
        cursor.execute(SQL_INSERT_USER, (groupUser.getIdUser(), groupUser.getId()))
        self.__db.commit()
        cursor.close()
        return 1

    def save(self, group):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_GROUP, (group.getName()))
        cursor._idGroup = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return 1
SQL_CREATE_GROUP = 'insert into groups_network(name, description) values (%s, %s)'
SQL_FIND_ID_BY_NAME = 'select id_group from groups_network where name like %s'
SQL_INSERT_USER = 'insert into users_groups (id_user, id_group) values (%s,%s)'
SQL_GET_GROUPS = 'select id_group, name, description from groups_network';
SQL_GET_USERS_IN_GROUP = 'select id_user from users_groups where id_group = %s'

class GroupDao:

    def __init__(self,db):
        self.__db=db

    def findIdByName(self, name):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_ID_BY_NAME, (name,))
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
        cursor.execute(SQL_CREATE_GROUP, (group.getName(), group.getDescription()))
        cursor._idGroup = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return 1

    def getGroups(self):        
        cursor = self.__db.cursor()
        cursor.execute(SQL_GET_GROUPS, )
        groups = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return groups

    def getUsersInGroup(self, idGroup):
        cursor = self.__db.cursor()
        cursor.execute(SQL_GET_USERS_IN_GROUP, (idGroup))
        users = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return users

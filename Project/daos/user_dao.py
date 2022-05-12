SQL_CREATE_USER = 'insert into users(uuid_user,name,password,email) values (%s,%s, %s, %s)'
SQL_FIND_BY_ID = 'select uuid_user,name, email, password from users where uuid_user = %s'
SQL_FIND_BY_UUID = 'select uuid_user,name, email, password from users where uuid_user = %s'
SQL_FIND_BY_EMAIL = 'select uuid_user from users where email = %s'
SQL_FIND_BY_NICKNAME = 'select uuid_user from users where name = %s'
SQL_UPDATE_PASSWORD = 'update users set password = %s where uuid_user=%s'

class UserDao:

    def __init__(self,db):
        self.__db=db

    def findByEmail(self, email):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_EMAIL, (email,))
        data = cursor.fetchone()
        return data

    def findByNickname(self, nickname):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_NICKNAME, (nickname,))
        data = cursor.fetchone()
        return data

    def findByUuid(self,uuid):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_UUID, (uuid,))
        data = cursor.fetchone()
        return data

    def findById(self, idUser):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_ID, (idUser,))
        data = cursor.fetchone()
        return data

    def save(self,user):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_USER, (user.getId() ,user.getNickname(),user.getPassword(),user.getMail()))
        cursor._id = cursor.lastrowid
        self.__db.commit()
        return cursor._id 
    
    def updatePassword(self,idUser,newPassword):
        cursor = self.__db.cursor()
        cursor.execute(SQL_UPDATE_PASSWORD,(newPassword,idUser))
        self.__db.commit()
        return idUser


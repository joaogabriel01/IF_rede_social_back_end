SQL_CREATE_USER = 'insert into users(name, password, email) values (%s, %s, %s)'
SQL_FIND_BY_ID = 'select id_user, name, email, password from users where id_user = %s'
SQL_FIND_BY_EMAIL = 'select id_user, name, email, password from users where email = %s'
SQL_FIND_BY_NICKNAME = 'select id_user, name, email, password from users where name = %s'
SQL_UPDATE_PASSWORD = 'update users set password = %s where id_user = %s'

class UserDao:

    def __init__(self,db):
        self.__db=db

    def findByEmail(self, email):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_EMAIL, (email,))
        data = cursor.fetchone()
        self.__db.commit()
        cursor.close()
        return data

    def findByNickname(self, nickname):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_NICKNAME, (nickname,))
        data = cursor.fetchone()
        self.__db.commit()
        cursor.close()
        return data


    def findById(self, idUser):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_ID, (idUser,))
        data = cursor.fetchone()
        self.__db.commit()
        cursor.close()
        return data

    def save(self,user):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_USER, (user.getNickname(),user.getPassword(),user.getMail()))
        cursor._id = cursor.lastrowid
        self.__db.commit()
        cursor.close()
        return cursor._id 
    
    def updatePassword(self,idUser,newPassword):
        cursor = self.__db.cursor()
        cursor.execute(SQL_UPDATE_PASSWORD,(newPassword,idUser))
        self.__db.commit()
        cursor.close()
        return idUser


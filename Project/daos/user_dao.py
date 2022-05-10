SQL_CREATE_USER = 'insert into usuarios(apelido,senha,email) values (%s, %s, %s)'
SQL_FIND_BY_ID = 'select id_usuario,apelido, email, senha from usuarios where id_usuario = %s'
SQL_FIND_BY_EMAIL = 'select id_usuario from usuarios where email = %s'
SQL_FIND_BY_NICKNAME = 'select id_usuario from usuarios where apelido = %s'
SQL_UPDATE_PASSWORD = 'update usuarios set senha = %s where id_usuario=%s'

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

    def findById(self, idUser):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_BY_ID, (idUser,))
        data = cursor.fetchone()
        return data

    def save(self,user):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_USER, (user.getNickname(),user.getPassword(),user.getMail()))
        cursor._id = cursor.lastrowid
        self.__db.commit()
        return cursor._id 
    
    def updatePassword(self,idUser,newPassword):
        cursor = self.__db.cursor()
        cursor.execute(SQL_UPDATE_PASSWORD,(newPassword,idUser))
        self.__db.commit()
        return idUser


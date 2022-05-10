SQL_CREATE_USER = 'insert into usuarios(apelido,senha,email) values (%s, %s, %s)'
SQL_FIND_EMAIL = 'select id_usuario from usuarios where email = %s'
SQL_FIND_USER = 'select id_usuario from usuarios where apelido = %s'

class UserDao:

    def __init__(self,db):
        self.__db=db

    def findByEmail(self, email):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_EMAIL, (email,))
        data = cursor.fetchone()
        return data

    def findByNickname(self, nickname):
        cursor = self.__db.cursor()
        cursor.execute(SQL_FIND_USER, (nickname,))
        data = cursor.fetchone()
        return data

    def save(self,user):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_USER, (user.getNickname(),user.getPassword(),user.getMail()))
        cursor._id = cursor.lastrowid
        self.__db.commit()
        return user
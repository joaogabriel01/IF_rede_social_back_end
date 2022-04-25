SQL_CREATE_USER = 'insert into usuarios(apelido,senha,email) values (%s, %s, %s)';

class UserDao:

    def __init__(self,db):
        self.__db=db

    def save(self,user):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CREATE_USER, (user.getNickname(),user.getPassword(),user.getMail()))
        cursor._id = cursor.lastrowid
        self.__db.commit()
        return user
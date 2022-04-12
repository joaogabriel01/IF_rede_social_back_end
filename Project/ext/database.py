from flaskext.mysql import MySQL

class Connection:

    def createConnection(app):
        mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = ''
        app.config['MYSQL_DATABASE_DB'] = 'denuncias'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        conn = mysql.connect()
        cursor = conn.cursor()
        return cursor

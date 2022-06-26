import os
from dotenv import load_dotenv
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

load_dotenv()

class Connection:

    def createConnection(app):
        mysql = MySQL(cursorclass=DictCursor)
        app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
        app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
        mysql.init_app(app)
        conn = mysql.connect()
        return conn

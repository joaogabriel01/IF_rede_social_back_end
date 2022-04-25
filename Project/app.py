from flask import Flask, render_template
from .routes.route_index import routes
from .ext.database import Connection
from .daos.user_dao import UserDao
from .models.user_model import User
from .controllers.user_controller import UserController


app = Flask(__name__)



routes.init_app(app)
db = Connection.createConnection(app)

@app.route('/')
def index():
    # cursor.execute("SELECT * from usuarios")
    # data=cursor.fetchone()
    # print(data)
    return render_template('login.html')

@app.route('/register')
def register():
    # cursor.execute("SELECT * from usuarios")
    # data=cursor.fetchone()
    # print(data)
    return render_template('register.html')



if __name__ == '__main__':
    app.run()
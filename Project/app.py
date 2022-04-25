from flask import Flask, render_template
from .routes.route_index import routes
from .ext.database import Connection
from .daos.user_dao import UserDao
from .models.user_model import User
from .controllers.user_controller import UserController


app = Flask(__name__)


db = Connection.createConnection(app)
routes.init_app(app,db)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



if __name__ == '__main__':
    app.run()
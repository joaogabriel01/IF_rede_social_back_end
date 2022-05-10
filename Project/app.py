from flask import Flask, render_template
from .routes.user_route import routes
from .ext.database import Connection

app = Flask(__name__)


db = Connection.createConnection(app)
routes.init_app(app,db)


if __name__ == '__main__':
    app.run()
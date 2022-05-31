from flask import Flask, render_template
from .routes.user_route import Routes as routesUser
from .routes.publication_route import Routes as routesPublications
from .routes.group_route import Routes as routesGroup
from .ext.database import Connection

app = Flask(__name__)


db = Connection.createConnection(app)
routesUser.init_app(app,db)
routesPublications.init_app(app,db)
routesGroup.init_app(app,db)


if __name__ == '__main__':
    app.run()
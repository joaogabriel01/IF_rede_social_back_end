from flask import Flask, render_template
from .routes.route_index import routes
from .ext.database import Connection

app = Flask(__name__)


db = Connection.createConnection(app)
routes.init_app(app,db)


@app.route('/')
def index():
    return render_template('intro/login_form.html')

@app.route('/register')
def register():
    return render_template('intro/register_form.html')



if __name__ == '__main__':
    app.run()
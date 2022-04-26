from flask import Flask, render_template
from .routes.user_route import routes
from .ext.database import Connection

app = Flask(__name__)


db = Connection.createConnection(app)
routes.init_app(app,db)


@app.route('/user/login')
@app.route('/')
def user_login():
    return render_template('intro/login_form.html')

@app.route('/user/register')
def user_register():
    return render_template('intro/register_form.html')

@app.route('/user/password_reset')
def user_password_reset():
    return render_template('intro/reset_password_form.html')

if __name__ == '__main__':
    app.run()
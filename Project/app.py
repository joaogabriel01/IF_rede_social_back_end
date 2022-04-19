from flask import Flask, render_template
from .routes.route_index import routes
from .ext.database import Connection


app = Flask(__name__)



routes.init_app(app)
cursor = Connection.createConnection(app)

@app.route('/')
def index():
    cursor.execute("SELECT * from usuarios")
    data=cursor.fetchone()
    print(data)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
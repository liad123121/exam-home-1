from flask import Flask
from database.mysql import init_db

from routes.home import bp as homeRouter
from routes.showdown import bp as showdownRouter

app = Flask(__name__)
init_db(app)

app.register_blueprint(homeRouter)
app.register_blueprint(showdownRouter)

if __name__ == '__main__':
    app.run()
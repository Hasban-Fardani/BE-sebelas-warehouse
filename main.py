# import modul
from flask import Flask
from flask_migrate import Migrate

from models.create_db import db
from models.user_model import UserModel

from controller import login_manager
from routes import blueprint

from dotenv import load_dotenv
from os import getenv

load_dotenv()

# create new flask app
app = Flask(__name__)

#
app.secret_key = getenv('APP_KEY')

# 
USERNAME = getenv('DB_USERNAME') or 'root'
PASSWORD = getenv('DB_PASSWORD') or ''
DATABASE = getenv('DB_DATABASE') or 'lapor_barang'
SERVER   = getenv('DB_SERVER')   or 'localhost'
PORT     = getenv('DB_PORT')     or 3306

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}"

# register blueprint
app.register_blueprint(blueprint)

# database init app
db.init_app(app)

#
login_manager.init_app(app)


# migrate database
Migrate(app, db)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


app.secret_key = f"c\xe0\xf8\xd1\x92\xc5/\xa2\xf14\xcdd[\xdb4\x9b"

db = SQLAlchemy()
migrate = Migrate(app,db)
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)

CORS(app)
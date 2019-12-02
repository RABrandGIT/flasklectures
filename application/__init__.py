from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  os import getenv
import pymysql
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DATABASE'))

#app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + 'root' + ':' + 'root' + '@' + '35.246.70.224' + '/' + 'Testbase')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = '7218a9143c27c16610765205a1b21cb7'


from application import routes


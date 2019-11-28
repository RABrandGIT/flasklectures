from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
db = os.getenv('MYSQL_DATABASE')
charset = 'utf8mb4'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://os.getenv('MYSQL_USER'):os.getenv('MYSQL_PASSWORD')@35.242.150.181/Testbase'
db = SQLAlchemy(app)

from application import routes


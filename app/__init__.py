from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://suvwdzryzaefyr:6461faddcdfecfd96bd277e63a7a1ecc36800411ed0fc35456c76698259c17c1@ec2-54-83-23-91.compute-1.amazonaws.com:5432/d33kv2ua1r2dg3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning



app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])

db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views

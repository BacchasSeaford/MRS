from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='Biggest Baddest Key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db=SQLAlchemy(app)
app.config.from_object(__name__)
from app import views

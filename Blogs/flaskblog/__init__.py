from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '9a3eb1fc019ae39d95cad0a74334829f'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:Vivek123@localhost/blogs'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
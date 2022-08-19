import os
from environs import Env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


env = Env()
env.read_env()
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
PORT = os.getenv("PORT")
db_host = str(os.getenv("ip"))

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}:{PORT}/{DATABASE}"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(APP)

#Import necessary libraries
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Import environment variables if env.py exists
if os.path.exists("env.py"):
    import env
    
#Create app and configure it
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
db = SQLAlchemy(app)

#Import routes
from Project import routes
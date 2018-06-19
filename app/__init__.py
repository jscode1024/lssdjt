from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/bosim"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "2bc7ed5efa9242fbbe5e40254cf66bde"
# db = SQLAlchemy(app)
from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404

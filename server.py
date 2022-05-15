# 📁 server.py -----
from os import environ as env

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask,render_template, session

from flask import Flask, request, render_template, request
from sqlalchemy.sql.expression import select
from os import path

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
oauth = OAuth(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/features")
def features():
        return render_template("features.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
        return render_template("contact.html")
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))
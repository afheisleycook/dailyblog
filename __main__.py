import pydoc
import secrets
import tempfile
import bs4
import requests
import sqlite3
from feedparser import FeedParserDict
from flask import Flask, render_template, request, request_started, redirect
import pymysql
app = Flask(__name__)
global current_feed
db = pymysql.Connection(host="localhost",user="dailylog",database="dailylog")
current_feed = {}
@app.route("/form")
def addform():
    return render_template("form.html")
@app.route("/")
def Home():
    conn = db.cursor()
    conn.execute("select * from log")
    data = conn.fetchall()
    return render_template("index.html",data=data)
@app.route("/feed",methods=["post"])
def submit_topic():
    title = request.form["title"]
    description = request.form["description"]
    tag = request.form["tag"]
    conn = db.cursor()
    conn.execute(f"insert into log values(0,'{title}','{description}','{tag}')")
    db.commit()
    try:

        return redirect("/")
    except Exception as e:
        error = e.args()
        return render_template("index.html",error=error)

@app.route("/search")
def Search():
    conn = db.cursor()
    query = request.args.get("title")

    conn.execute(f"select log_id, log_description, log_tag from log where logtitle='{query}'")
    data = conn.fetchall()
    return render_template("index.html",data=data)


app.run(host="0.0.0.0",debug=True)
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import json

DATABASE = "database.db"

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config["DATABASE"])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cur = g.db.execute("select name, score from current_scores order by score desc")
    scores = [dict(position=i+1, name=row[0], score=row[1]) for i, row in enumerate(cur.fetchall())]
    return render_template("home.html", scores=scores)

@app.route("/scores", methods=["POST"])
def post_scores():
    g.db.execute("delete from current_scores")
    print request.json
    print request.form

    if request.json:
        data = request.json
    elif request.form:
        data = json.loads(request.form["json"])


    for entry in data:
        values = [entry["name"], entry["score"]]
        g.db.execute("insert into current_scores (name, score) values (?, ?)", values)
    g.db.commit()
    return "OK"

if __name__ == "__main__":
    init_db()
    port = 80 if os.getuid() == 0 else 8080
    debug = os.getuid() != 0
    app.run(debug=debug, host="0.0.0.0", port=port)

from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("pets2_db")
    pets = mysql.query_db("select * from pets;")
    print(pets)
    return render_template("index.html", pets = pets)

@app.route("/post", methods = ["POST"])
def post_new():
    mysql = connectToMySQL("pets2_db")
    query = "insert into pets(name, type)values(%(nm)s, %(tp)s);"
    data = {
        'nm': request.form["name"],
        'tp': request.form["type"]
    }
    mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
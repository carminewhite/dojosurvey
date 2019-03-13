from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():


    return render_template("index.html")


@app.route('/addnew', methods=['POST'])
def form():
    query = "INSERT INTO dojosurvey.ninja (name, locations, languages, comment) VALUES (%(nm)s, %(lc)s, %(ln)s, %(cmt)s);"
    
    data = {
        "nm" : request.form["name"],
        "lc" : request.form["location"],
        "ln" : request.form["language"],
        "cmt" : request.form["comment"]
    }

    mysql = connectToMySQL('dojosurvey')
    mysql.query_db(query, data)
    print(data)

    return render_template('show.html', ninjas = data)





if __name__ == "__main__":
    app.run(debug=True)
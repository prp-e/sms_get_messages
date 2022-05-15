from flask import Flask, request
import json
import os
import sqlite3
from uuid import uuid4

DATABASE = os.path.join('.', 'db.sqlite3')
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/getMessage', methods=["POST"])
def getMessage():
    if request.method == "POST":
        input_data = request.data
        json_data = json.loads(input_data)
        try:
            cur = get_db().cursor()
            cur.execute('INSERT INTO messages (from_number, to_number, message) VALUES (?, ?, ?)', (json_data['from'], json_data['to'], json_data['message']))
            cur.close()
            return {'msg' : 'success'}, 200
        except Exception as e:
            print(e)
            return {'msg' : 'fail'}, 400 
    
if __name__ == '__main__':
    app.run(debug=True)
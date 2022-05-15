from flask import Flask, request
import json
import sqlite3

db = sqlite3.connect('db.sqlite3')

app = Flask(__name__)

@app.route('/getMessage', methods=["POST"])
def getMessage():
    if request.method == "POST":
        input_data = request.data
        json_data = json.loads(input_data)
        try:
            cur = db.cursor()
            cur.execute('INSERT INTO messages VALUES (?, ?, ?)', (json_data['from'], json_data['to'], json_data['message']))
            cur.close()

            return {'msg' : 'success'}, 200
        except:
            return {'msg' : 'fail'}, 400 
    
if __name__ == '__main__':
    app.run(debug=True)
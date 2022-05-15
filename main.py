from flask import Flask, request, g
import json
import os
import sqlite3
from uuid import uuid4

app = Flask(__name__)

@app.route('/getMessage', methods=["POST"])
def getMessage():
    if request.method == "POST":
        input_data = request.data
        print(input_data)
        json_data = json.loads(input_data)
        try:
            f = open('result.txt', 'a')
            f.write(f'{json_data["from"]}, {json_data["to"]}, {json_data["message"]} \n')
            return {'msg' : 'success'}, 200
        except Exception as e:
            print(e)
            return {'msg' : 'fail'}, 400 
    
if __name__ == '__main__':
    app.run(debug=True)
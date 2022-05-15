from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/receive', methods=["POST"])
def receive():
    pass

if __name__ == '__main__':
    app.run(debug=True)
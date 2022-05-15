from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/getMessage', methods=["POST"])
def getMessage():
    if request.method == "POST":
        input_data = request.data
        json_data = json.loads(input_data)
        print(json_data)
    return {'msg' : 1}
    
if __name__ == '__main__':
    app.run(debug=True)
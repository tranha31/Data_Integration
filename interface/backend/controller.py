from functools import partial
from tkinter.messagebox import NO
from flask import Flask, request, jsonify
from flask.wrappers import Response
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from bl import BL
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/phone", methods=['GET'])
@cross_origin()
def getPhone():
    r = request
    r = r.args
    name = r.get("name")
    rom = r.get('rom')
    ram = r.get('ram')
    currentPage = r.get("currentPage")
    if name == None:
        name = ""
    if rom == None:
        rom = ""
    if ram == None:
        ram = ""
    bl = BL()
    result = bl.filter(name, rom, ram, currentPage)
    result = json.dumps(result, ensure_ascii=False)
    
    return Response(response=result, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
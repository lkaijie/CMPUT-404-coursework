from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

TODOs = {
    1:{"task":"build an API"},
    2: {"task" : "????"},
    3: {"task" : "profit"},
}


class HelloWorld(Resource):
    def get(self):
        return {"hello":"world"}
    
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
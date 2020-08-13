from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'name': 'nassar', 'age': '20'}

    def post(self):
        jsonInput = request.get_json()
        return {'u sent': jsonInput}, 201


class Add(Resource):
    def get(self, num):
        return {'result': num + 1}


class Cloud():
    def get(self):
        return {'A': '7A'}


api.add_resource(HelloWorld, '/')
api.add_resource(Add, '/add/<int:num>')
api.add_resource(Cloud, '/nassartest1.git')

if __name__ == '__main__':
    app.run()

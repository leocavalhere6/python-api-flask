from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

Devs = []

class Dev(Resource):
    def get(self, id: any):
        return Devs
    def post(self):
        data = json.loads(request.data)
        data['id'] = len(Devs)
        Devs.append(data)
        return 'Postando'

api.add_resource(Dev, '/dev')

if __name__ == '__main__':
    app.run(debug=True)
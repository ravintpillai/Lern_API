from flask import Flask, request
from flask.ext.restful import Resource, Api

from algorithms import *

app = Flask(__name__)
api = Api(app)

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world 1'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world 2'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world 3'}, 201, {'Etag': 'some-opaque-string'}

class LogisticRegressions(Resource):
    def get(self):
        params = logistic_regression(pandas.read_csv("tumor_size.csv").as_matrix()).params
        results={}
        for x in range(len(params)):
            if x == len(params)-1:
                results['constant']=params[x]
            else:
                results['coefficient '+str(x)]=params[x]
        return results

api.add_resource(Todo1, '/')
api.add_resource(Todo2, '/hey')
api.add_resource(Todo3, '/yo')
api.add_resource(LogisticRegressions, '/log')

if __name__ == '__main__':
    app.run(debug=True)

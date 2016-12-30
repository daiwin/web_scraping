# -*- coding: utf-8 -*-
import dataset
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_restful.utils import cors

db = dataset.connect('postgresql://postgres:root@localhost:5432/postgres')
table = db['facts']
results=''

app = Flask(__name__)
api = Api(app, decorators=[cors.crossdomain(origin='*')])

class TodoSimple(Resource): 
    

    def get(self, word):
        #return {'hello': 'world'}
        data =[]
        results = table.find(word = word.lower()) 
        for row in results:
            data.append({'dt':row['dt'],'count':row['count']})
         
        return json.dumps({"mass":data})

api.add_resource(TodoSimple, '/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)










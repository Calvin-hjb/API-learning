from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #default writing to Flask app
api = Api(app)

names = {"tim": {"age": 19, "gender": "Male"},
         "jess": {"age": 26, "gender": "Female"}}

class HelloWorld(Resource): # Make a class that can handle resoruce 
    def get(self, name):
        return names[name]
    

api.add_resource(HelloWorld, "/helloworld/<string:name>") # add.resource(resource, key) key is the url; can add argument into it



if __name__ == "__main__": # To start server and application 
    app.run(debug=True) # To turn on the debugging (for testing environment, for actual situation dont turn it on)

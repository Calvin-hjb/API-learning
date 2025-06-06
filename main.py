from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #default writing to Flask app
api = Api(app)


class HelloWorld(Resource): # Make a class that can handle resoruce 
    def get(self, name, test):
        return {"name": name, "test":test} # should be written in dictionaries. the return should be jason serializeable object
    
    #def post(self):
    #    return {"data": "posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>") # add.resource(resource, key) key is the url and / is default url



if __name__ == "__main__": # To start server and application 
    app.run(debug=True) # To turn on the debugging (for testing environment, for actual situation dont turn it on)

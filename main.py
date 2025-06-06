from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) #default writing to Flask app
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True) #reqparse will return these messages when the input is not what it supposed to
video_put_args.add_argument("views", type=int, help="Views of the video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required = True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}


api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__": # To start server and application 
    app.run(debug=True) # To turn on the debugging (for testing environment, for actual situation dont turn it on)

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__) #default writing to Flask app
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True) #reqparse will return these messages when the input is not what it supposed to
video_put_args.add_argument("views", type=int, help="Views of the video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required = True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Videos id is not valid...")

def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message = "Video already exist with that ID...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #201 is a response for "created"

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__": # To start server and application 
    app.run(debug=True) # To turn on the debugging (for testing environment, for actual situation dont turn it on)

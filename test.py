import requests

BASE = "http://127.0.0.1:5000/"

#get can be change into post, put, delete
response = requests.get(BASE+"helloworld/tim/19")
print(response.json()) # use .json to let the response object be somekind of information
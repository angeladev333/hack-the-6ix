from flask import Flask
from flask_restful import Api, Resource
from roboflow import Roboflow
import requests


app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    data ={
        'Type':'Person',
        'Age':18
    }
    return data

@app.route('/yolo')
def yolo():
    rf = Roboflow(api_key="KnKjHINSt6Is99kC3IXv")
    project = rf.workspace().project("vision-artificial-dataset")
    model = project.version(1).model

    # infer on a local image
    results = model.predict("server\\multiple_parts.jpg", confidence=10, overlap=30).json()
    results = results.get('predictions')
    parts = []
    for item in results:
        parts.append(item.get("class"))
    parts = list(set(parts))
    return parts

@app.route('/generate_page')
def generate_page():
    return "Hello World"

@app.route('/generate_image')
def generate_image():
    return "Hello World"

@app.route('/upload_to_ipfs')
def upload_to_ipfs():
    file = open("server\\multiple_parts.jpg", "rb")
    response = requests.post(
        "https://api.nftport.xyz/v0/files",
        headers={"Authorization": '4eee2cb8-3210-407c-9d3f-fbb8dcf09995'},
        files={"file": file}
    )
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
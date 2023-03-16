from flask import Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import base64

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'


@app.route('/request/get-seismo')
def seismo(data=[]):
    url = 'https://bpptkg.esdm.go.id/pub/sismogram.php'
    page = requests.get(url)
    scraper = BeautifulSoup(page.content, "html.parser")
    data_containers = scraper.find_all("div", class_="panel-primary")

    for data_element in data_containers:
        title = data_element.find("div", class_="panel-heading").text
        image = data_element.find(
            "div", class_="panel-body").find("img")['src']
        wrapper = {'title': title, 'image': image}

        data.append(wrapper)

    return data


@app.route('/request/get-camera-merapi')
def cameraMerapi(data=[]):
    url = 'https://bpptkg.esdm.go.id/viewer_images/view.php?id=22'
    base64_data = base64.b64encode(requests.get(url).content).decode("utf-8")

    return jsonify(base64_data)


@app.route('/request/get-camera-merbabu')
def cameraMerbabu(data=[]):
    url = 'https://bpptkg.esdm.go.id/viewer_images/view.php?id=79'
    base64_data = base64.b64encode(requests.get(url).content).decode("utf-8")

    return jsonify(base64_data)


@app.route('/request/get-thermal')
def cameraThermal():
    url = 'https://bpptkg.esdm.go.id/viewer_images/view.php?id=106'
    base64_data = base64.b64encode(requests.get(url).content).decode("utf-8")

    return jsonify(base64_data)

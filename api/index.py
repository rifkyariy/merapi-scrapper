from flask import Flask
import requests
from bs4 import BeautifulSoup

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
        wrapper = {
            'title': title,
            'image': image
        }

        data.append(wrapper)

    return data


@app.route('/request/get-camera-merapi')
def seismo(data=[]):
    url = 'https://bpptkg.esdm.go.id/viewer_images/view-r.php?id=22&screen=1'
    page = requests.get(url)
    scraper = BeautifulSoup(page.content, "html.parser")
    data = scraper.find("img")['src']

    return data


@app.route('/request/get-camera-merbabu')
def seismo(data=[]):
    url = 'https://bpptkg.esdm.go.id/viewer_images/view-r.php?id=79&screen=2'
    page = requests.get(url)
    scraper = BeautifulSoup(page.content, "html.parser")
    data = scraper.find("img")['src']

    return data


@app.route('/request/get-thermal')
def seismo(data=[]):
    url = 'https://bpptkg.esdm.go.id/viewer_images/view-r.php?id=106&screen=7'
    page = requests.get(url)
    scraper = BeautifulSoup(page.content, "html.parser")
    data = scraper.find("img")['src']

    return data

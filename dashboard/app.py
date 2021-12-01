from flask import Flask, render_template
from db import Database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')


@app.route('/api/device-load')


@app.route('/api/environment')
def get_api_environment():
    return {"error": "Route note implemented",
            "temperature": None,
            "pressure": None,
            "humidity": None, }


@app.route('/api/temperature')
def get_api_temperature():
    return {"error": "Route note implemented",
            "temperature": None,
            "pressure": None,
            "humidity": None, }


@app.route('/api/pressure')
def get_api_pressure():
    return {"error": "Route note implemented",
            "temperature": None,
            "pressure": None,
            "humidity": None, }


@app.route('/api/humidity')
def get_api_humidity():
    return {"error": "Route note implemented",
            "temperature": None,
            "pressure": None,
            "humidity": None, }


if __name__ == '__main__':
    app.run()

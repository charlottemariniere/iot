from flask import Flask, render_template, jsonify
from db import CPU, Storage, Base, EnvironmentTPH
from flask_cors import CORS

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


import random
# import logging
# import current as current
# import self as self

db_filename = './data/monitor_data.db'
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

engine = create_engine(f'sqlite:///{db_filename}')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)


def set_status(status):
    if status is True:
        return 'All good', 'fa fa-smile', 'bg-success'
    elif status is False:
        return 'Not working', 'fas fa-angry', 'bg-danger'
    else:
        return 'Unknown error', 'fas fa-sad-tear', 'bg-dark'


@app.route('/')
def index():
    # check to see if cpu-monitor is running
    monitor_cpu = True
    # check to see if storage monitor is running
    monitor_storage = False
    # check to see if environmental monitor is running
    monitor_enviro = None

    # set up component dictionaries and set values
    cpu = {}
    cpu['name'], cpu['icon'] = 'CPU', 'fa-microchip',
    cpu['message'], cpu['emoticon'], cpu['class'] = set_status(monitor_cpu)

    storage = {}
    storage['name'], storage['icon'] = 'Storage', 'fa-hdd'
    storage['message'], storage['emoticon'], storage['class'] = set_status(
        monitor_storage)

    enviro = {}
    enviro['name'], enviro['icon'] = 'Enviro', 'fa-leaf'
    enviro['message'], enviro['emoticon'], enviro['class'] = set_status(
        monitor_enviro)

    statuses = [cpu, storage, enviro]
    return render_template('index.html', statuses=statuses)





@app.route('/about')
def demo_template():
    return render_template('about.html')


@app.route('/api/cpu-load/<qty>')
def cpu_load(qty=1):
    try:
        qty = abs(int(qty))
    except:
        qty = 1
    active_session = session()
    cpu = active_session.query(CPU).order_by(CPU.created_at.desc()).first()
    data = {cpu.id:{
        'host_name':cpu.host_name,
        'created_at': cpu.created_at,
        'load':cpu.load
    }}
    return jsonify(data)


@app.route('/api/cpu-load')
def cpu_load_latest():
    return cpu_load(1)


@app.route('/api/device-load')
def return_current_cpu():
    data = current_cpu()
    return {"CPU": data}


@app.route('/api/environment')
def get_api_environment():
    current_environment = get_api_temperature(), get_api_pressure(), get_api_humidity()
    return {"Environment": current_environment}


@app.route('/api/temperature')
def get_api_temperature():
    current_temperature = EnvironmentTPH().temperature
    return {"Temperature": current_temperature}


@app.route('/api/pressure')
def get_api_pressure():
    current_pressure = EnvironmentTPH().pressure
    return {"Pressure": current_pressure}


@app.route('/api/humidity')
def get_api_humidity():
    current_humidity = EnvironmentTPH().humidity
    return {"Humidity": current_humidity}


@app.route('/api/history')
def temp_history():
    @app.route('/api/ticker')
    def random_number_ticker():
        x = 0
        for num in range(1):
            random_number = random.randint(0, 100)
            x = random_number
            return {"History": x}
    return render_template("history.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)
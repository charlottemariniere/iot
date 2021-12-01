from datetime import datetime
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import CPU, Storage, Base

from mypi import \
    get_serial, get_mac, get_host_name, \
    get_cpu_temp, get_gpu_temp, get_maximum_cpu_load

import sqlite3
from db import EnvironmentTPH, Base
import mypi

db_filename = './data/monitor_data.db'
app = Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})


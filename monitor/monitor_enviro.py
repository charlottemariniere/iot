import random
import logging
import current as current

import self as self

from flask import Flask, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from db import CPU, Base, EnvironmentTPH

db_filename = './data/monitor_data.db'
app = Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})

